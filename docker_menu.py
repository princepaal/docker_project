import os
import getpass
apass = "prince"
count=0
while count < 3:
	passwd = getpass.getpass("                                          Enter password")
	if apass !=passwd:
		print("TRy again ...Enter wrong password:")
		count+=1
	else:
		while True:
			os.system("clear")
			print("""
                                                                    Welcome to docker world
                                                                   *************************
                                                                        docker images 
                                                                        *************
          
		1: Create the yum-configuration			2: Install docker		3: Create Image
		
		4: Launch operating system 			5: Remove all container         6: Create your own image
                 
                 ***********************************************About containers*****************************************
                                            
								7: Start container 

								8: Stop container						
	      						
								9:Terminate container

		                         ********************* Infrastructure*******************

		10: Launch Wordpress				11:Launch jenkins


 

			""")

			ch = int(input("Enter your choice. "))

			if ch==1:
				os.system("cp epel.repo dock.repo  epel-playground.repo epel-	testing.repo root.repo rpmfusion-free-updates.repo   rpmfusion-free-updates-testing.repo /etc/yum.repos.d/ ")
				print("Hey sir /mam now your yum is configured check by 'yum repolist'  ")			
			elif ch==2:	
			 	os.system("yum install docker-ce --nobest -y") 
			
			elif ch==3:
				image_name = input("Enter the image name with version like centos:7 or ununtu:14.04")
				os.system("docker pull {}".format(image_name))
				print("{} image download Succesfully")
			elif ch==4:
				os_name = input("Launch operating system for EX- centos:7 or ubuntu:14.04 ")
				os.system("docker run -it {} ".format(os_name))
				print("Hey sir /mam your operating system is launched ")
			elif ch==5:
				os.system("docker container rm -f $(docker container ps -a -q ) ")
		                
			elif ch==6:
				os.system("docker images")
				jname=input('\nContainer Name : ')
				img_name = input('Enter image name with version. for ex- centos:7 : ')
				os.system("docker run -dit --name {} {}".format(jname,img_name))
			elif ch==7:	
				
				os.system("docker ps -a")
				start = input("Container Name : ")
				os.system("docker start {}".format(start))
				print("{} container start successfully.".format(start))
				x=input("Enter to continue...")

			elif ch==8:
				os.system("docker ps")
				stop = input("Container Name : ")
				os.system("docker stop {}".format(stop))
				print("{} container stopped successfully.".format(stop))
				x=input("Enter to continue...")
			elif ch==9:
				os.system("docker ps -a")
				terminate = input("Container Name : ")
				os.system("docker stop {}".format(terminate))
				print("{} container terminated successfully.".format(terminate))
				x=input("Enter to continue...")
			
			elif ch==10:
				os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
				os.system("chmod +x /usr/local/bin/docker-compose")
				os.system("cp docker-compose.yml /") 
				os.system("cd / ")
				os.system("mkdir /infrastructure")
				os.system("cd /infrastructure/")
				os.system("pwd")
				os.system("mv ../docker-compose.yml .")
				os.system("docker-compose up -d")
				print("Wordpress is ready to use. Run Wordpress in browser with Base OS IP and port no. : 8080. for ex- 192.168.43.139:8080")
				x=input("""
	  			Details :
					MYSQL_ROOT_PASSWORD : redhat
					MYSQL_USER : prince
					MYSQL_PASSWORD : redhat
					MYSQL_DATABASE : db
					Container : prince
					Image : mysql:5.7
					Press Enter to continue...""")

			elif ch==11:
				os.system("docker images")
				jname=input('\nContainer Name : ')
				img_name = input('Enter image name with version. for ex- centos:7 : ')
				os.system("docker run -dit --name {} {}".format(jname,img_name))
				print("downloading jenkins....")
				os.system("sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo")
				os.system("sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key")
				os.system("yum install jenkins")
				print("Jenkins is ready to use. Run Jenkins in browser with Container IP and port no. : 8080. for ex- 	192.168.43.151:8080")
				print("""
				Details :
					Container : {0}
					Image : {1}	""".format(jname,img_name))

				print("{} container created successfully.".format(jname))
				x=input("Enter to continue...")
	
				

				

















