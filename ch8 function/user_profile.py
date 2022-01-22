def user_profile(first,last,**user_info):
    user_info["first_name"]=first.title()
    user_info["last_name"]=last.title()
    print(user_info)
user_profile("mohamed ali","jmal",country="Tunisia",vision="to work",his_duty="improve himself")
