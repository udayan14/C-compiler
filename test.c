void main()
{
	int *f,*g,*a,*b;
	
	*f=*f+33;
	*f=*g+42;
	*f=*f+21;

	if(!(*a<3 &&*b<*a && *b<*g)){
		*b=*b+*a;
		*b=*b+*a * 3;	
	}
	*f=*f+33;
	*f=*g+42;
	*f=*f+21;
	while(f<g){
		*f=*f+3;
		*f=*g+4;
		*f=*f+2;
		if(f==g){
			*a = *a + 1;
			*b = *b + 2;
		}
		else{
			*a = *a + 3;
		}
		*f=*f+3;
		*g=*g+11;
	}
	if(*a<*b)
		if(*a>*b)
			if(*a != *b)
				*a=*b+21;
			else{
				*b = *b +*a * *f;
				*a = *b +*a * *g;
			}


	*f=*f+12345;
	*f=*f+123678;

	if(*f<*g);
	*f=*f+123;
	
	if(*f > *g)
		*b = *a + 112;

	while(*f > *g){
		*a = *a + 1;
		*b = *b + 2;
	}
}