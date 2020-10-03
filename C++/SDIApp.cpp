#include <iostream>
using namespace std;

//Prototype functions
void binomialApproximation();
void poissonApproximation();

class Binomial
{
public:
    double sampleSize;
    double successProbability;
    Binomial(double n,double p)
    {
        sampleSize = n;
        successProbability = p;
    }
    void display()
    {
        cout<<"Binomial";
    }
};

class Poisson
{
public:
    double lambda;
    Poisson(double l)
    {
        lambda = l;
    }
    void display()
    {
        cout<<"Poisson";
    }
};

int main()
{
    int dist;
    double n,p,l;

    while(true)
    {
        cout<<"Select a distribution you want approximate"<<endl;
        cout<<"     1 - Binomial"<<endl;
        cout<<"     2 - Poisson"<<endl;
        cin>>dist;

        switch(dist)
        {
        case 1:
            cout<<"Enter sample size (n): ";
            cin>>n;
            cout<<"Enter success probability (p): ";
            cin>>p;
            break;

        case 2:
            break;
        }
    }

    return 0;
}

void binomialApproximation()
{
}

void poissonApproximation()
{
}
