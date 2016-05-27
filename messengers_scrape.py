def get_data(messengers, playstore):

    final_data = dict()
    base_url = "https://play.google.com/store/apps/details?id="

    for app, url in messengers.items():
        final_data[app] = playstore.get_playstore_info(base_url + url)

    return final_data


def get_messengers():

    messengers = dict()
    messengers["whatsapp"]  = "com.whatsapp"
    messengers["messenger"] = "com.facebook.orca"
    messengers["viber"]     = "com.viber.voip"
    messengers["skype"]     = "com.skype.raider"
    messengers["hike"]      = "com.bsb.hike"
    messengers["telegram"]  = "org.telegram.messenger"

    return messengers
    
