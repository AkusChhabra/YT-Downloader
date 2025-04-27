import os
import subprocess
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download():

    url = input("Enter a YouTube video URL: ")
    output_extension = "mp4"
    output_path = "./../downloads"

    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        if not yt:
            raise Exception('Unable to resolve YouTube URL.')

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ver_id = 1
        output_filename = yt.title
        
        while os.path.isfile(f"{output_path}/{output_filename}.{output_extension}"):
            if "_" in output_filename[-2:]:
                old_ver_id = int(output_filename[-1:]) + 1
                output_filename = f"{output_filename[:len(output_filename)-2]}_{old_ver_id}"
            else:
                output_filename = f"{output_filename}_{ver_id}"
            ver_id += 1

        vStream = yt.streams.get_highest_resolution(False)

        if not vStream.is_progressive:
            aStream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

            if not aStream:
                raise Exception('No audio stream found.')
            
            v_path = vStream.download(filename="v.mp4")
            a_path = aStream.download(filename="a.mp3")

            subprocess.run(['ffmpeg','-i', v_path,'-i', a_path,'-c:v', 'mpeg4','-preset','ultrafast',
                            '-crf', '22', '-c:a', 'aac','-pix_fmt','yuv420p',
                            f'{output_path}/{output_filename}.{output_extension}'])
            
            os.remove(v_path)
            os.remove(a_path)

            print(f"Video has been downloaded as: {output_filename}.{output_extension} to the folder {output_path}")
        else:
            vStream.download(filename=f"export_video.{output_extension}",output_path=output_path)
            print(f"Video has been downloaded as: export_video.{output_extension} to the folder {output_path}")
    except Exception as e:
        print(f"An error has occurred: {e}")

#if __name__ == "__main__":
#    download()