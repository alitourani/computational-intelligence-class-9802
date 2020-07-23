//created by amir.cph4
//20 july 2020
#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

void main() {
	struct house {
		string mahalle;
		int metrazh;
		bool parking;
		bool asansor;
		int salsakht;
		int otaghkhab;
		int price;
	};
	house houseList[300];
	string a[] = { "golshahi","motahari","resalat","golestan" };
	string b[] = { "emam ali","sahar","razi","boostan" };
	string c[] = { "sahand","pakdasht","ettehad","rezvan" };
	for (int i = 0; i < 300; i++) {
		if (i < 100) {
			houseList[i].mahalle = a[rand() % 4];
			houseList[i].metrazh = rand() % (130 - 60 + 1) + 60;
			houseList[i].parking = rand() % 2;
			houseList[i].asansor = rand() % 2;
			houseList[i].salsakht = rand() % (1398 - 1393 + 1) + 1393;
			houseList[i].otaghkhab = rand() % 3 + 1;
		}
		else if (i < 200) {
			houseList[i].mahalle = b[rand() % 4];
			houseList[i].metrazh = rand() % (130 - 60 + 1) + 60;
			houseList[i].parking = rand() % 2;
			houseList[i].asansor = rand() % 2;
			houseList[i].salsakht = rand() % (1398 - 1393 + 1) + 1393;
			houseList[i].otaghkhab = rand() % 3 + 1;
		}
		else if (i < 300) {
			houseList[i].mahalle = c[rand() % 4];
			houseList[i].metrazh = rand() % (130 - 60 + 1) + 60;
			houseList[i].parking = rand() % 2;
			houseList[i].asansor = rand() % 2;
			houseList[i].salsakht = rand() % (1398 - 1393 + 1) + 1393;
			houseList[i].otaghkhab = rand() % 3 + 1;
		}
	}
	int prePrice;
	for (int i = 0; i < 300; i++) {
		prePrice = 0;
		if (houseList[i].mahalle == "golshahi" || houseList[i].mahalle == "motahari" || houseList[i].mahalle == "resalat" || houseList[i].mahalle == "golestan") {
			switch (houseList[i].salsakht)
			{
			case 1393:
				prePrice = 2500000;
				break;
			case 1394:
				prePrice = 2800000;
				break;
			case 1395:
				prePrice = 3100000;
				break;
			case 1396:
				prePrice = 3700000;
				break;
			case 1397:
				prePrice = 4000000;
				break;
			case 1398:
				prePrice = 4500000;
				break;
			}
			if (houseList[i].asansor) {
				prePrice += 500000;
			}
			if (houseList[i].parking) {
				prePrice += 200000;
			}
			switch (houseList[i].otaghkhab)
			{
			case 3:
				prePrice += 400000;
				break;
			case 2:
				prePrice += 200000;
				break;
			case 1:
				prePrice += 100000;
				break;
			}
			houseList[i].price = prePrice * houseList[i].metrazh;
		}
		else if (houseList[i].mahalle == "emam ali" || houseList[i].mahalle == "sahar" || houseList[i].mahalle == "razi" || houseList[i].mahalle == "boostan") {
			switch (houseList[i].salsakht)
			{
			case 1393:
				prePrice = 2000000;
				break;
			case 1394:
				prePrice = 2300000;
				break;
			case 1395:
				prePrice = 2600000;
				break;
			case 1396:
				prePrice = 3200000;
				break;
			case 1397:
				prePrice = 3500000;
				break;
			case 1398:
				prePrice = 4000000;
				break;
			}
			if (houseList[i].asansor) {
				prePrice += 500000;
			}
			if (houseList[i].parking) {
				prePrice += 200000;
			}
			switch (houseList[i].otaghkhab)
			{
			case 3:
				prePrice += 400000;
				break;
			case 2:
				prePrice += 200000;
				break;
			case 1:
				prePrice += 100000;
				break;
			}
			houseList[i].price = prePrice * houseList[i].metrazh;
		}
		else {
			switch (houseList[i].salsakht)
			{
			case 1393:
				prePrice = 1500000;
				break;
			case 1394:
				prePrice = 1800000;
				break;
			case 1395:
				prePrice = 2100000;
				break;
			case 1396:
				prePrice = 2700000;
				break;
			case 1397:
				prePrice = 3000000;
				break;
			case 1398:
				prePrice = 3500000;
				break;
			}
			if (houseList[i].asansor) {
				prePrice += 500000;
			}
			if (houseList[i].parking) {
				prePrice += 200000;
			}
			switch (houseList[i].otaghkhab)
			{
			case 3:
				prePrice += 400000;
				break;
			case 2:
				prePrice += 200000;
				break;
			case 1:
				prePrice += 100000;
				break;
			}
			houseList[i].price = prePrice * houseList[i].metrazh;
		}
	}
	ofstream myfile;
	myfile.open("house.csv");
	myfile << "mahalle,masahat,parking,asansor,salsakht,otaghkhab,price\n";
	for (int i = 0; i < 300; i++) {
		myfile << houseList[i].mahalle << "," << houseList[i].metrazh << "," << houseList[i].parking << "," << houseList[i].asansor << "," << houseList[i].salsakht << "," << houseList[i].otaghkhab << "," << houseList[i].price << "\n";
	}
	myfile.close();
}