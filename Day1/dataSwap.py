# By SasanAce.tech on https://github.com/Sana-Allah-Kheiri | https://www.linkedin.com/in/sasanace/ | https://www.youtube.com/@sasanace
# ==========================
# Swaping string & numeric data between two variables
# ==========================
retry = 1;

def exitF():
    print("Exiting app after 3 seconds...");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    sys.exit("Goodbye!")


def retryF():
    retry = input(" Type 0 to exit | Type 1 to restart");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;
        
while(retry == 1):
    def swap_function (a , b):
        t = a;
        a = b;
        b = t;
        print('********');
        print("a:" , a);
        print('********');
        print("b:" , b);
        print('********');

    a = input('a: ');
    b = input('b: ');
    swap_function(a, b);
    retryF();