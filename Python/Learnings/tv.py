#TV Class

class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0 #constant
        self.VOLUME_MAXIMUM = 10 #constant
        self.volume = self.VOLUME_MAXIMUM #integer divide

    def power(self):
        self.isOn = not self.isOn #toggle
        
    def volumeUp(self):
        if not self.isOn:
            return
        
        if self.isMuted:
            self.isMuted = False # changing the volume while muted unmutes the sound
            
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        
        if self.isMuted:
            self.isMuted = False # changig the volume while muted unmutes the soud
            
        if self.volume < self.VOLUME_MINIMUM:
            self.volume = self.volume -1

    def channelUp(self):
        if not self.isOn:
            return
        
        self.channelIndex = self.channelIndex + 1

        if self.channelIndex > self.nChannels:
            self.channelindex = 0 # wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        
        self.channelIndex = self.channelIndex - 1

        if self.channelIndex < self.nChannels:
            self.channelindex = self.nChannels - 1 # wrap around to the first channel

    def mute(self):
        if not self.isOn:
            return

        self.isMuted = not self.isMuted # Toggle

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
            # if channel is already in the list it will do nothing

    def showInfo(self):
        print('\nTV Status:')
        if self.isOn:
            print('\tTV is: On')
            print('\tChannel is: ', self.channelList[self.channelIndex])
            if self.isMuted:
                print('\tVolume is: ', self.volume, ' (sound is muted)')
            else:
                print('\tVolume is: ', self.volume)
        else:
            print('\tTV is: Off')
                
            
            
