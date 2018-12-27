import re
import netmiko
from getpass import getpass
import sys

'''
A small script to send primary/Secondary/Tertiray config lines
to a list of Access Points within a controller
'''


def check_ip(ip_address):
    '''
    A small function to ensure correct IP addressing format/number.
    '''
    # Lets now define the IP regex
    ip_regex = ('^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
                '(\.(?!$)|$)){4}$')
    # Let's compile it:
    ip_pattern = re.compile(ip_regex)

    # Check the address is correct!
    while True:
        if re.search(ip_pattern, ip_address):
            return ip_address
        else:
            ip_address = input('Sorry, Wrong IP, try again: ')

def main():
    # How many controllers?
    if len(sys.argv) < 2 or int(sys.argv[1]) > 3:
        print('Enter 1, 2 or 3 HA controllers. ')
        sys.exit()

    # Specific to Cisco Default Naming Convention.
    def_regex = (r'^AP([0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4})?')
    def_cisco_wap_name = re.compile(def_regex)

    # Let's get some Variables in place.
    mgmt_wlc_ip = check_ip(input('Managing Controller IP  Address? '))
    username = input('Username? ')
    password = getpass('Password? ')

    # Lets get some info and commands built.
    p_controller_name = input("Primary controller's Name? ")
    p_controller_ip = input("Primary Controller's IP? ")
    # Build the 'send' command:
    p_command = 'config ap' + ' ' + 'primary_base' + ' ' \
                + p_controller_name + ' '

    if sys.argv[1] == '2':
        s_controller_name = input("Secondary Controller's Name? ")
        s_controller_ip = input("Seconday Controller's IP? ")
        # Build the 'send' for secondary if exists.
        s_command = 'config ap' + ' ' + 'secondary_base' + ' ' \
                    + s_controller_name + ' '
    if sys.argv[1] == '3':
        t_controller_name = input("Tertiary Controller's Name? ")
        t_controller_ip = input("Tertiary Controller's IP? ")
        # Build the 'send' command for Tertiray if exists.
        t_command = 'config ap' + ' ' + 'secondary_base' + ' ' \
                    + t_controller_name + ' '
    '''
    Now that we have some input data, we can now start connecting
    to the managing controller for WAPs.
    '''
    # Get list of WAPs.
    while True:
        try:
            # Connect to device
            nc = netmiko.ConnectHandler(ip=mgmt_wlc_ip,
                                        device_type='cisco_wlc',
                                        username=username,
                                        password=password)
            # Get full list of WAPs
            ap_list = nc.send_command('show ap summary').splitlines()[8:]
            nc.disconnect()
            break
        except ValueError:
            print('Wrong Username or Password')
            username = input('Username? ')
            password = getpass('Password? ')
        except netmiko.ssh_exception.NetMikoTimeoutException:
            mgmt_wlc_ip = input('Wrong MGMT WLC Address. Please re-enter')

    # Trim it to Names only.
    print("The controller is reporting the following WAPS: ")
    ap_names = [ap.split(' ',1)[0] for ap in ap_list]

    # Print it for administrator.
    for ap in ap_names:
        print(ap)

    # End it by summing the total number of WAPs.
    print('Total of: ' + str(len(ap_list)) + ' ' + 'WAPs')
    '''
    Getting which WAPs is a little tricky. Cisco, if not configured,
    would give WAPs a default name in for mat AP1234.1234.1234.
    We need to be able to differentiate between such default names and
    waps actually configured with AP in them. For example R.ACSC.AP001.

    This bit also allowes Partial, yet case sensitive selection.
    '''
    while True:
        which_waps = input(('Which WAPs? Partial is OK.'
                            '"default" for auto named, or all. '
                            'CaSe senstive. '))
        # This is where we make our selection.
        if 'default' in which_waps:
            select_waps = [ap for ap in ap_names
                           if re.match(def_cisco_wap_name, ap)]
            break
        elif 'all' in which_waps.lower():
            select_waps = [ap for ap in ap_names]
            break
        else:
            select_waps = [ap for ap in ap_names
                           if which_waps in ap]
            if len(select_waps) == 0:
                print("Sorry. Can't find any wap. Try again. ")
            else:
                break

    # Connect to device
    # nc = netmiko.ConnectHandler(ip=mgmt_wlc_ip, device_type='cisco_wlc',
    #                             username=username, password=password)

    # Lets build it and print it!
    for ap in select_waps:
        set_command = p_command + ap + ' ' + p_controller_ip
        if sys.argv[1] == '2':
            set_command = s_command + ap + ' ' + s_controller_ip
        elif sys.argv[1] == '3':
            set_command = t_command + ap + ' ' + t_controller_ip


if __name__ == '__main__':
    main()
