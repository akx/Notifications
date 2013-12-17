import glob, subprocess, os
ffmpeg = os.environ.get("FFMPEG", "ffmpeg")

for wav in glob.glob("*.wav"):
	ogg = os.path.splitext(wav)[0] + ".ogg"
	if os.path.exists(ogg):
		continue
	command = [
		ffmpeg,
		"-i",
		wav,
		"-acodec", "libvorbis",
		"-aq", "100",
		"-map_metadata", "-1",
		ogg
	]
	subprocess.check_call(command)