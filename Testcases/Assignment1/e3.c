void main()
{
	int a;
	int b;
        int *p, *q;
 
        p = &a, q = &b;
	*p = *q = *p = *p = 3;
}
