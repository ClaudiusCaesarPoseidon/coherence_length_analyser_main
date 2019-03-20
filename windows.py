import scipy.signal


def window(window='boxcar', width=480):
    exceptions = ['kaiser', 'gaussian', 'general_gaussian', 'slepian',
                  'dpss', 'chebwin', 'exponential', 'tukey']
    if window not in exceptions:
        return scipy.signal.get_window(window, width, fftbins=False)
    elif window == 'kaiser':
        return scipy.signal.get_window((window, 15), width, fftbins=False)
    elif window in ['slepian', 'dpss']:
        return scipy.signal.get_window((window, 0.02), width, fftbins=False)
    elif window == 'gaussian':
        return scipy.signal.get_window((window, 0.4 * (width - 1) / 2), width, fftbins=False)
    elif window == 'chebwin':
        return scipy.signal.get_window((window, 100), width, fftbins=False)
    elif window == 'exponential':
        return scipy.signal.get_window((window, int(width/2), 50), width, fftbins=True)
    elif window == 'tukey':
        return scipy.signal.get_window((window, 0.6), width, fftbins=True)



#scipy.signal.kaiser(480, 15)
#y = scipy.signal.slepian(width, 0.02)
#x = scipy.signal.gaussian(width, 0.4 * (width - 1) / 2)

"""boxcar, triang, blackman, hamming, hann, bartlett,
flattop, parzen, bohman, blackmanharris, nuttall, barthann, kaiser (needs beta),
gaussian (needs standard deviation), slepian (needs width),
dpss (needs normalized half-bandwidth), chebwin (needs attenuation), exponential (needs decay scale), tukey (needs taper fraction)"""


from matplotlib import pyplot as plt


plt.plot(window('boxcar'))
plt.show()
plt.plot(window('triang'))
plt.show()
plt.plot(window('blackman'))
plt.show()
plt.plot(window('hamming'))
plt.show()
plt.plot(window('hann'))
plt.show()
plt.plot(window('bartlett'))
plt.show()
plt.plot(window('flattop'))
plt.show()
plt.plot(window('parzen'))
plt.show()
plt.plot(window('bohman'))
plt.show()
plt.plot(window('blackmanharris'))
plt.show()
plt.plot(window('nuttall'))
plt.show()
plt.plot(window('barthann'))
plt.show()
plt.plot(window('kaiser'))
plt.show()
plt.plot(window('gaussian'))
plt.show()
plt.plot(window('slepian'))
plt.show()
plt.plot(window('chebwin'))
plt.show()
plt.plot(window('exponential'))
plt.show()
plt.plot(window('tukey'))
plt.show()