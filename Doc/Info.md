## Cel
---
program ma przewidywać liczbę strzelonych goli w meczu

### **Dane** 
---
które program będzie brał pod uwagę dane z poprzeninnch meczów aktualnej tableli:

*D - dana dotepna w tabeli

 1. Ostatnie 5 meczów ligowych (określenie w jakiej formie jest dany zespół)
    1. Tabela formy druzyny
         1. Przeciwnik
         2. Poziom przeciwnika ogólny (średnia zrobytych punktów)
         3. Liczba goli zdobytych
         4. Liczba xGf (expected gols for)
         5. Liczba goli straconych
         6. Liczba xGa (expected gols against) 
         7. Liczba strzałów
         8. Liczba strzałów celnych
         9. Posiadanie piłki (okreśnienie czy druzyna dominowała, ale tak pozornie [nie wiem czy to jest potrzebne])
         10. Wynik (3pkt-zwyciestwo, 1pkt remis, 0pkt porazka)
          ---
          Podsumowanie

         1. Suma punktów
         2. Procent zdobytych punktów        

 2. Ostatnie 5 meczów z druzynami na poziomie najblizszego rywala na podstawie liczby punktów
    1. Tabela z druzynami na poziomie najblizszego rywala 
         1. Przeciwnik
         2. Poziom przeciwnika ogólny (średnia zrobytych punktów)
         3. Liczba goli zdobytych
         4. Liczba xGf (expected gols for)
         5. Liczba goli straconych
         6. Liczba xGa (expected gols against) 
         7. Liczba strzałów
         8. Liczba strzałów celnych
         9. Wynik (3pkt-zwyciestwo, 1pkt remis, 0pkt porazka)
         ---
          Podsumowanie

         1. Suma punktów
         2. Procent zdobytych punktów  

 3. Statystyki z sezonu poszczególnej druzyny
     1. Tabela statystyk poszczegolnej druzyny (kolejność nieprzypadkowa, w takiej ma być tabela)
          1. Nazwa | D
          2. Liczba strzelonych goli | D
          3. Liczba straconych goli | D
          4. Expected gols for | D
          5. Expected gols for na 90 min | D
          5. Expected gols against | D
          6. Liczba strzałów | D
          7. Liczba strzałów celnych | D
          8. Statystyki na 90 min (2-7) | D
          9. Staytyki domowe (2,3,4,5) | D
          11. Statystyki na wyjezdzie (2,3,4,5) | D

     2. Tabela statystyk vsDana_druzyna

          1. Nazwa druzyny (nie przecinwik)
          2. Liczba strzelonych goli | D
          3. Liczba straconych goli | D
          4. Expected gols | D
          6. Liczba strzałów
          7. Liczba strzałów celnych
          8. Statystyki na 90 min (2-7)
          9. Staytyki domowe (2-7)
          10. Statystyki domowe na 90 min (2-7)
          11. Statystyki na wyjezdzie (2-7)
          12. Statystyki na wyjezdzie na 90 min(2-7)

 4. Statystyki z sezonu wszystkich druzyn
    1. Statystyki karnych
         1. Liczba rzutów karnych
         2. Liczba rzutów karnych na 90 min
         3. Liczba wykorzystanych rzutow karnych
         4. Liczba wykorzystanych rzutow karnych na 90 min
    2. Statystyka rzutów roznych
         1. Liczba rzutów roznych
         2. Liczba rzutów roznych na 90 min
         3. Liczba rzutow karnych prowadząca do zdobycia bramki
         4. Liczba rzutow karnych prowadząca do zdobycia bramki na 90 min
 




