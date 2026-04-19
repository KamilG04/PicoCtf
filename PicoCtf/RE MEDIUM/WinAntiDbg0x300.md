W ida nic ciekawego mnostwo funckji sama binarka byla spakowana 
jest napewno security cookie ale czy o to chodzi czas odpalic windbg

![[Pasted image 20260419161753.png]]

![[Pasted image 20260419183916.png]]

Wiec zanim sie wywali 
![[Pasted image 20260419183951.png]]

Wola 
Nic tutaj ciekawego nie ma jest jakis const sprawdzanie tej binarki bardzo porozrzucana duzo syscalli ale jest jakis plik pdb wczesniej odpakowalem upxem 
Plik z rozszerzeniem **.pdb** (Program Database) to głównie ==plik binarny używany przez Microsoft Visual Studio do przechowywania informacji o debugowaniu projektu, ułatwiający naprawę błędów i śledzenie kodu==. W nauce, format ten (Protein Data Bank) reprezentuje trójwymiarowe struktury cząsteczek biologicznych, takich jak białka.
Nie wiedzialem o tym
Teraz wyglada to duzo lepiej w Ghidrze

void __cdecl ManageChildProcess(int param_1,wchar_t **param_2)

{
  int iVar1;
  char *pcVar2;
  undefined4 uVar3;
  ulong uVar4;
  
  ComputeHash(1);
  MUTEX = (void *)CreateMutexW(0,0,szTitle);
  if (MUTEX == (void *)0x0) {
    MessageBoxW(0,L"[FATAL ERROR] Failed to create the Mutex. Challenge aborted.",szTitle,0x10);
    Terminate(0xff);
  }
  iVar1 = GetLastError();
  if (iVar1 == 0xb7) {
    if (param_1 != 2) {
      OutputDebugStringW(
                        L"[ERROR] Exactly two arguments expected by the Child process. Exiting...\n"
                        );
      MessageBoxW(0,L"Check if the program is already running.",szTitle,0x10);
      CloseHandle(MUTEX);
      Terminate(0xff);
    }
    pcVar2 = WCharToChar(param_2[1]);
    if (pcVar2 == (char *)0x0) {
      OutputDebugStringW(L"Error converting WChar to Char.\n");
      CloseHandle(MUTEX);
      Terminate(0xff);
    }
    uVar3 = atoi(pcVar2);
    iVar1 = DebugActiveProcess(uVar3);
    if (iVar1 == 0) {
      uVar4 = atoi(pcVar2);
      uVar4 = getParentProcessID(uVar4);
      iVar1 = OpenProcess(1,0,uVar4);
      if (iVar1 == 0) {
        CloseHandle(MUTEX);
        free(pcVar2);
        OutputDebugStringW(L"Error opening a handle to debuggerPID.\n");
        Terminate(0xff);
      }
      iVar1 = TerminateProcess(iVar1,0);
      if (iVar1 == 0) {
        OutputDebugStringW(L"Failed to terminate the debugger process.\n");
        free(pcVar2);
        CloseHandle(MUTEX);
        Terminate(0xfe);
      }
      else {
        OutputDebugStringW(L"Debugger process terminated successfully.\n");
        free(pcVar2);
        CloseHandle(MUTEX);
        Terminate(0xfd);
      }
    }
    else {
      OutputDebugStringW(L"No debugger was present. Exiting successfully.\n");
      uVar3 = atoi(pcVar2);
      DebugActiveProcessStop(uVar3);
      CloseHandle(MUTEX);
      free(pcVar2);
      Terminate(0);
    }
    Terminate(0);
  }
  ComputeHash(1);
  return;
}


Tutaj jest to co nam niszczy debugowanie

void __cdecl ComputeHash(int param_1)

{
  uint uVar1;
  uint uVar2;
  int local_10;
  int local_c;
  
  uVar1 = FLAG_SIZE;
  for (local_10 = 0; local_10 < param_1; local_10 = local_10 + 1) {
    for (local_c = 0; local_c < (int)uVar1; local_c = local_c + 1) {
      uVar2 = (local_c % 0xff & 0x55U) + (local_c % 0xff >> 1 & 0x55U);
      uVar2 = (uVar2 & 0x33) + ((int)uVar2 >> 2 & 0x33U);
      HASH[local_c] =
           (char)((int)((HASH[local_c] - 0x61) + (uVar2 & 0xf) + ((int)uVar2 >> 4)) % 0x1a) + 'a';
    }
  }
  return;
}
to nasza flage bierze chyba z tego jak wyzej wogole te ciasteczko security 

void __cdecl DecryptFlag(uchar *param_1)

{
  uint local_8;
  
  for (local_8 = 0; local_8 < FLAG_SIZE; local_8 = local_8 + 1) {
    FLAG[local_8] = FLAG[local_8] ^ param_1[local_8];
  }
  return;
}

Kilka nopow zamiast tam przy while check i klasa ale nwm czy o to chodzilo probojac to debugowac ominiecie tej petli jest bardzo trudne spatchowanie jej tez w x32dbg jeszcze bardziej.

![[Pasted image 20260419201709.png]]