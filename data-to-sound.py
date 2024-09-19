import binascii
import pyaudio

a = open('/home/ian/Python-programs/modem/testy_mcTest.txt', 'rb')
c = a.read()
b = bin(int(binascii.hexlify(c), 16))

sample_stream = []
high_note = (b'\xFF'*100 + b'\0'*100) * 50
low_note = (b'\xFF'*50 + b'\0'*50) * 100
for bit in b[2:]:
    if bit == '1':
        sample_stream.extend(high_note)
    else:
        sample_stream.extend(low_note)


sample_buffer = ''.join(map(str, sample_stream))

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(1),
                channels=1,
                rate=44100,
                output=True)
stream.write(sample_buffer)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()