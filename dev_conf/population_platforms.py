import os


def populate():
    icecream_platform = add_platform('Icecream', '172.17.2.151', '172.17.32.204', 'spb')

    add_device('VLE', '00:80:09f:A0:38:EF', '135.247.58.243', 'artems', 'OT', icecream_platform)


    # Print out what we have added to the user.
    for c in Platform.objects.all():
        for p in Device.objects.filter(platform=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_device(type, mac, ip, owner, connect_to, platform):
    p = Device.objects.get_or_create(type=type, mac=mac, ip=ip, owner=owner,
                                     connect_to=connect_to, platform=platform)[0]
    return p

def add_platform(name, ot_ip, oxe_ip, location):
    c = Platform.objects.get_or_create(name=name, ot_ip=ot_ip, oxe_ip=oxe_ip, location=location)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Platforms population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_conf.settings')
    from platforms.models import Platform, Device
    populate()
