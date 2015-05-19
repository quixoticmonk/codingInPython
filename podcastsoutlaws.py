from urllib import *
#To learn how to download files form a certain urllib module

def main():
	for i in range ( 100,371):
		urlretrieve("http://www.podtrac.com/pts/redirect.mp3/traffic.libsyn.com/linuxoutlaws/linuxoutlaws%d.mp3"%i,'C:\Python27\Test_files\linuxoutlaws%d.mp3'%i)


if __name__ == "__main__":
	main()


