#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]) {
	
	float Qsera;
	float Aortu;
	char ortu[10];
	char ay[9]= {'Ekim','Kasim','Aralik','Ocak','Subat','Mart','Nisan','Mayis','Haziran'};
	int Ataban = 25000 ;
	float U;//U aylýk ortalama sýcaklýk farkýna göre degisecek, bunu aylara göre tanimlayip isleme nasil katarim? Sor.
	int Tic=18;
	float Tdis;//ortalama Tdis aylara göre degisecek, bunu aylara göre tanimlayip isleme nasil katarim? Sor.
	//Formulde Sera kurulan yerin en düþük ortalama dýþsýcaklýk deðeri [°C] verilmis.
	//kas icin 13 derece, aksu icin 12.35, serik icin 10.4 derece olur.
	char ilce[3];
	float I; //aksu,serik ve kas icin toplam gunes isinimi
	float T; //toplam isik gecirgenligi
	int katman;
	
	Qsera=((Aortu/Ataban)*U*(Tic-Tdis)-I*T*0.9352)*Ataban; 
	//Birimi [Watt/m^2*m^2]'dir. Yani aslinda Q nokta ile göstermek gerekir.	
	
	printf( "Ilceyi secin(a/s/k)\n" );
	scanf( "%s", &ilce);
	if(ilce[3]="a"){
		I=218.75;
	}
	else{
		I=227.08;
	}
	printf( "Ortu malzemesini seciniz(pe/pvc/hg/pc)\n" );
	scanf( "%s", &ortu);

	if(ortu[10]="hg"){
		Aortu=30512.5;
		T=0.89;	
	}
	else if(ortu[10]="pe"){
		Aortu=31712.5;
		T=0.86;
	}
	else if(ortu[10]="pvc"){
		Aortu=31712.5;
		T=0.91;
	}
	else if(ortu[10]="pc"){
		Aortu=31712.5;
		T=0.78;
	}
	
	printf("Ortu katman sayisini seciniz(1/2)\n");
	scanf( "%d", &katman);
	
	//Ýlceye ve aylara gore U ve sicaklik farkini excel dosyasindan alacak ve gerekli guc degerlerini her ilce,ay,kaplama malzemesi
	//katman sayisi icin hesaplayacak.
	if(katman=1){
		if(ortu[10]="hg"){U = 4.1;
		}
		else if(ortu[10]="pe"){U = 4.7;
		}
		else if(ortu[10]="pvc"){U = 4.6;
		}
		else if(ortu[10]="pc"){U = 4.3;}
	}
	else if(katman=2){
		if(ortu[10]="hg"){U = 1.5;
		}
		else if(ortu[10]="pe"){U = 2.3;
		}
		else if(ortu[10]="pvc"){U = 2.1;
		}
		else if(ortu[10]="pc"){U = 2.3;}
	}
	
	printf( "%s malzemesi ile ortulu sera icin gereken ortalama guc %f olur.", ortu, Qsera);
	return 0;
}
