import requests

def transfer():
    #print('heello')
    mavenpath=' /home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar '
    jfrogpath=' http://18.144.23.229:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar '
    username = 'admin'
    password ='Jfrog123$' 

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



    
    
