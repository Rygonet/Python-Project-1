# Python-Project-1
Projekta uzdevums:
Dotā projekta mērķis ir automatizēt kādu no ikdienas uzdevumiem. Es esmu kultūrists, kurš ar katru nedēļu uzņemas svarā, lai paliktu stiprāks. Tādēļ liela daļa no manas ikdienas tiek veltīta treniņiem, svara uzturēšanai un ēdienu pētīšanai, jo diezgan bieži ēst vienu un to pašu paliek ļoti garlaicīgi. Tieši tāpēc kā savu ikdienas uzdevumu, vai šajā gadījumā uzdevumus, es izvēlējos automatizēt:
1. kaloriju daudzuma aprēķināšanu, cik man jāapēd dienā lai uzturētu savu svaru;
2. jaunu recepšu meklēšanu;
3. apēsto kaloriju piefiksēšanu Excel failā.
Šī projekta kodu es varēšu lietot vairākas reizes dienā, jo galvenā pamatideja ir tāda: Es pamostos no rīta, nosveros, un ar 1. funkcijas palīdzību nosaku cik man šodien ir jāapēd kaloriju, lai saglabātu savu tagadējo svaru. Lai uzņemtos svarā man tajā dienā ir vienkārši jāapēd vairāk nekā izdot kods. Tā kā vakarā es parasti sagatavoju maltīti visai nākamajai dienai (parasti sanāk 6-8 porcijas), ar 2. funkcijas palīdzību es varēšu ne tikai izvēlēties ko es gatavošu, bet arī uzzināt visas nianses par iedomāto maltīti. No 2. funkcijas es dabūšu pilnu ingredientu sarakstu, recepti un uzturvērtības, ko es varēšu pārkopēt no termināla uz telefonu, lai varētu pa dienu iepirkties un vakarā no telefona lasot, gatavot. Noslēdzot dienu, pirms gulēt iešanas es varēšu saglabāt pa dienu piefiksēto apēsto kaloriju skaitu excel failā, lai man būtu vieglāk izsekot savu progresu vai noteikt nepilnības, ja tādas radīsies.


Izmantotās bibliotēkas:
1. Selenium. Selenium bibliotēka tika izmantota, lai varētu ar pārlūka "Chrome" palīdzību automatizēt darbības veiktas "https://www.allrecipes.com" vietnē. Tālāk no Selenium bibliotēkas tika importēts Webdriver, no kura savukārt tika importētas funkcijas kā Service, By un Keys, kas man turpmāk atviegloja automatizācijas procesu un palīzēja atrisināt jaunas problēmas. Kā piemērs: Tika ievadīti vēlamie ingridienti meklēšanā joslā, bet nevarēja uzspiest meklēšanas pogu, jo tā tika identificēta kā attēls, bet ar Keys palīdzību varēja vienkārši uzspiest tastatūras pogu ENTER un tādā veidā veikt meklēšanu.
2. Time. Time bibliotēka tika izmantota, lai dotu kodam "atpūsties" un pagaidīt kamēr ielādēsies mājaslapa pirms veikt turpmākās darbības.
3. Openpyxl un Workbook. Openpyxl un Workbook bibliotēkas tika izmantotas lai kods varētu lasīt, rakstīt un kopumā strādāt ar Microsoft Excel failu.
4. Datetime. Datetime bibliotēka tika izmantota lai varētu vielgāk formatēt un noteikt šodienas datumu.


Izmantotās metodes:
Tiek izmantotas 3 metodes. Izvēloties tās, lietotājs norāda galvenajā programmā "a", "b" vai "c" burtus. Tas tika sasniegts izmantojot if, elif un else blokus. Pēdējais else bloks izmet ķļūdu, ja netika pareizi ievadīts viens no trim burtiem.

Kaloriju kalkulatora, jeb "a" metode:
Šī metode tiek izmantota, lai aprēķinātu cik kalorijas lietotājam ir jāapēd dienā, pamatojoties uz ievadītajiem dzimuma, vecuma, auguma un svara datiem.
Metode izmanto matemātiskus aprēķinus, lai noteiktu Basal Metabolic Rate (BMR), un tad ar ievadītajiem fiziskās aktivitātes līmeņu datiem, aprēķinātu Active Metabolic Rate (AMR), jeb kaloriju skaitu, cik ir jāapēd dienā, lai saglabātu savu tagadēju svaru. Formulas ņemtas no vietnes "https://www.verywellfit.com/how-many-calories-do-i-need-each-day-2506873"

Recepšu meklēšanas, jeb "b" metode:
Šī metode tiek izmantota, lai meklētu jaunas receptes, pamatojoties uz ievadītajiem produktiem.
Izmanto Selenium bibliotēku, lai automatizētu pārlūkprogrammu un veiktu darbības vietnē "https://www.allrecipes.com".
Lietotājam tiek uzdoti jautājumi par produktiem, pēc tam tiek veikta meklēšana un tad ar "for" cikla palīdzību lietotājam tiek izvadīts saraksts no 8 receptēm.
Lietotājam tiek prasīts izvēlēties recepti 0-7, un pēc izvēles tiek izvadīta detalizēta informācija par izvēlēto recepti.

Šodien apēsto kaloriju piefiksēšanas, jeb "c" metode:
Šī metode tiek izmantota, lai piefiksētu šodien apēsto kaloriju daudzumu Excel failā.
Izmanto Openpyxl bibliotēku, lai lasītu, rakstītu un saglabātu Excel failu.
Izmanto datetime bibliotēku, lai noteiktu šodienas datumu.
Pārbauda, vai jau ir veikts ieraksts šodien, un, ja nav, pievieno jaunus datus ar šodienas datumu un apēsto kaloriju daudzumu.
