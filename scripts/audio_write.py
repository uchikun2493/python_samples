import numpy as np
import pyaudio 
import wave

if __name__=='__main__':
    REC_TIME = 5
    FILE_PATH = "output.wav" #音声を保存するファイル名
    FMT = pyaudio.paInt16  # 音声のフォーマット
    CH = 1              # チャンネル1(モノラル)
    SAMPLING_RATE = 44100 # サンプリング周波数
    CHUNK = 2**11       # チャンク（データ点数）
    AUDIO = pyaudio.PyAudio()
    INDEX = 0 # 録音デバイスのインデックス番号（デフォルト1）

    stream = audio.open(format=FMT,
                        channels=CH,
                        rate=SAMPLING_RATE,
                        input=True,
                        input_device_index=INDEX,
                        frames_per_buffer=CHUNK)
    print("recording start...")
    
    # 録音処理
    frames = []
    for i in range(0, int(sampling_rate / chunk * rec_time)):
        data = stream.read(chunk)
        frames.append(data)

    print("recording  end...")

    # 録音終了処理
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 録音データをファイルに保存
    wav = wave.open(file_path, 'wb')
    wav.setnchannels(ch)
    wav.setsampwidth(audio.get_sample_size(fmt))
    wav.setframerate(sampling_rate)
    wav.writeframes(b''.join(frames))
    wav.close()

