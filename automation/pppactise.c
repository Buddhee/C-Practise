#include <stdio.h>
int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    int sum;
    int lastDigit=0;
    while(n!=0)
    {
        int lastDigit=n%10;
        if (n%2==0)
        {
            sum=sum+lastDigit;
            n=n/10;
        }
    
    }
    printf("The sum of all even digits is: %d",sum);
    return 0;
}