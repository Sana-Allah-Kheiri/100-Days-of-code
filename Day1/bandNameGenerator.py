# By Sasan Ace on https://github.com/Sana-Allah-Kheiri
# In this project as Dr Yu told us we are going to generate a name based on pet & city names
retry = 1;
while (retry==1):
    print('Hey there 😊 So you need a band name right? /n');
    UserName = input('Whats your name?');
    print ('Ok dear ' , UserName);
    cityName = input('Whats the name of city where you born?');
    print ('So dear ', UserName , ' you born in beautiful city of ' , cityName , ' sounds cool');
    petName = input ("but whats your pet's name ? ");
    #final result is suggesting a silly name by concatinating pet & name
    print("============================================== ");
    print(" I suggest these two names for your rock band 👇 ");
    print (" " , cityName + " " + petName);
    print (" " , petName + " " + cityName);
    print("============================================== ");
    retry = input('\n Type 1 to restart | Type 0 to exit');
    retry = int(retry);
print("/n See you later🤙");
print("/n Dont forget how to run python scripts in GitBash 👇");
print("1st <Locate python file path> 2nd run 'python filename.py' ");