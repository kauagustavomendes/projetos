print("\x1b[2J\x1b[1;1H")

while True:
    num = (int(input("digite um numero:")))
    print(("-----")*4)
    print("[X] para cancelar")
    print("[1] base binaria")
    print("[2] base octal")
    print("[3] base decimal")
    print("[4] base hexadecimal")
    print("[5] base ascII")
    print(("-----")*4)
    esc = (input("escolha uma opção de conversão:"))
    
    if esc  in "x" "X":
        print("aplicação cancelada")
        break
    elif esc in ("1" "2" "3" "4" "5"):
        if esc == "1":
            print(bin(num))
        elif esc == "2":
            print(oct(num))
        elif esc == "3":
            print(num)
        elif esc == "4":
            print(hex(num))
        elif esc == "5":
            print(chr(num))
    else:
            print("\033[0;31m opção invalida!")
    
