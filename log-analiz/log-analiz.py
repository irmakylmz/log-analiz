def log_analiz(log_listesi):
    info = 0
    warning = 0
    error = 0

    for satir in log_listesi:
        if "INFO" in satir:
            info += 1
        elif "WARNING" in satir:
            warning += 1
        elif "ERROR" in satir:
            error += 1

    print("--- LOG ANALİZ RAPORU ---")
    print("INFO:", info)
    print("WARNING:", warning)
    print("ERROR:", error)
    print("------------------------")


def main():
    try:
        with open("system.log", "r", encoding="utf-8") as dosya:
            loglar = dosya.readlines()
            log_analiz(loglar)

    except FileNotFoundError:
        print("system.log bulunamadı")


main()