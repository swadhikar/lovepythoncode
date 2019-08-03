def log_celcius(function):
    """Logs fahrenheit temperature in celcius"""
    def wrapper(city, f_temp):
        function(city, f_temp)             # function call
        c_temp = (f_temp - 32) * (5 / 9)   # code conversion
        print('({:.2f} deg. C)'.format(c_temp))
    return wrapper                         # returns callable


@log_celcius                               # log_celcius(log_f_temp)
def log_f_temp(city, f_temp):
    """ Logs Fahrenheit temperature """
    print('{} had "{:.2f}" deg. F'
          .format(city, f_temp), end=' ')


log_f_temp('Chennai', 104)  # Chennai had "104.00" deg. F (40.00 deg. C)
log_f_temp('Madurai', 100)  # Madurai had "100.00" deg. F (37.78 deg. C)
    
