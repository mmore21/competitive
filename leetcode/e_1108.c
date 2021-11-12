/*
Problem: 1108 - Defanging an IP Address
Difficulty: Easy
URL: https://leetcode.com/problems/defanging-an-ip-address/
*/

char *defangIPaddr(char *address)
{
    char *res = (char *) calloc(strlen(address) + 7, sizeof(char));
    
    int k = 0;
    for (int i = 0; address[i] != '\0'; i++)
    {
        if (address[i] == '.')
        {
            res[k++] = '[';
            res[k++] = '.';
            res[k++] = ']';
        }
        else
        {
            res[k++] = address[i];
        }
    }
        
    res[k] = '\0';
    return res;
}
