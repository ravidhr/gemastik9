#include <stdio.h>
#include <stdlib.h>

int is_access_code_correct(char input[32]) {
  FILE *db;
  char access_code[64];
  db = fopen("PowerPlant.db", "r");
  fread(&access_code, 1, 64, db);
  fclose(db);
  if (strcmp(input, access_code) == 0) {
    return 1;
  }
  return 0;
}

void enter_power_plant_system() {
  FILE *fp;
  char flag[64];
  fp = fopen("PowerPlant2.flag", "r");
  fread(&flag, 1, 64, fp);
  fclose(fp);
  printf("       %s\n\n", flag);
}

int main() {
  printf("\n");
  printf(" __          ________ _      _____ ____  __  __ ______              ,/\n");
  printf(" \\ \\        / /  ____| |    / ____/ __ \\|  \\/  |  ____|           ,'/\n");
  printf("  \\ \\  /\\  / /| |__  | |   | |   | |  | | \\  / | |__            ,' /\n");
  printf("   \\ \\/  \\/ / |  __| | |   | |   | |  | | |\\/| |  __|         ,'  /_____,\n");
  printf("    \\  /\\  /  | |____| |___| |___| |__| | |  | | |____      .'____    ,' \n");
  printf("     \\/  \\/   |______|______\\_____\\____/|_|  |_|______|          /  ,'\n");
  printf("                                                                / ,'\n");
  printf("  =====================================================        /,'\n");
  printf("           - Power Plant Control System v2.0 -                /'\n");                                        
  printf("\n\n\n");
  printf("       SECRET ACCESS CODE : ");

  char input[32];
  scanf("%s", input);

  printf("\n\n");

  if (is_access_code_correct(input)) {
  	printf("       ACCESS GRANTED\n\n");
  	enter_power_plant_system();
  } else { 
    printf("       ACCESS DENIED\n\n");
  }

  return 0;
}
