import requests
#import os 
#import stat

def transfer():
    #print('heello')
    #mavenpath=' /home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar '
    mavenpath='/var/lib/jenkins/workspace/jfdemo/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar' 
    jfrogpath='http://54.176.189.61:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password ='Jfrog123$' 
    #os.chmod(mavenpath, stat.S_IROTH|stat.S_IWOTH|stat.S_IXOTH)
    with open (mavenpath,'rb') as mpath:
        res=requests.put(jfrogpath,auth=(username,password),data=mpath)

    if res.status_code == 200:
        print('File transferred successfully')
    else:
        print(f'file transfer failed with {res.status_code} and {res.text} ')

def main():
    transfer()
    #print('Hello')

if __name__ == '__main__':
    main()



    
    
