def car(manufacturer,model,**kwargs):
    kwargs["manufacturer"]=manufacturer
    kwargs["model"]=model
    return kwargs
print(car('subaru', 'outback', color='blue', tow_package=True))