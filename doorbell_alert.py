import doorbell_pushover as pushover
import time
import os

def alert(cfg):
	# Output to Local Screen
	print (time.strftime("%d/%m/%Y %H:%M:%S")) + " " + cfg["message"]
	# Play a sound through the speaker
	if cfg["localsound"]:
		os.system("mpg123 -q " + cfg["mp3"] + " &")
	# Send notification through pushover
	if cfg["pushover"]:
		pushover.send(cfg["pushover_app_token"],
		cfg["pushover_user_token"],
		cfg["pushover_title"],
		cfg["message"],
		cfg["pushover_url"])	
	# Take a picture
	img=""
	if cfg["camera"]:
		img=takepicture(cfg)
		# Upload to ftp
		if cfg["ftp_upload"]:
			ftp.upload(cfg,img)
	# Log to mysql
	if cfg["log_to_mysql"]:
		mysql.save(cfg,img)

	return