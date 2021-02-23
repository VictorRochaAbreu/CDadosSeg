Obtenha ao menos 10 APKs de, no mínimo, três categorias diferentes (https://www.apkmirror.com/categories/) para compor seu dataset cru
Para cada APK coletada, extraia o arquivo AndroidManifest.xml em um diretório "manifests", lembrando de identificar o arquivo resultante (por exemplo, se sua APK se chama 'BancoX-v01.apk', nomeie o manifesto como 'AndroidManifest_BancoX-v01.xml').
Escreva um script em Python (ou um ipynb) que, dado um diretório como argumento de entrada, retorne a lista de permissões de cada AndroidManifest.xml sob a forma de um dicionário (chave: nome da APK, valor: lista de permissões). Exemplo de saída impressa no terminal desta parte do script:

No mesmo script, faça uma função que retorne a lista de permissões únicas de cada APK e comuns a todas as APKs analisadas (intersecção). Exemplo de saída impressa no terminal desta parte do script:

No script da parte 1 abaixo temos um exemplo de entrada onde por um argumento na linha de comandos é passado um diretorio onde precisa conter apenas arquivos .xml ao qual o programa vai ler e listar, permissões de cada APK, permissões unicas de cada APK e as permissões em comum de todas as APKs

C:\Users\Victor\Desktop\CIENCIA DE DADOS SEGURANÇA>python T2p1a.py Manifest

--                  --
--    PERMISSÕES    --
--     POR  APK     --
--                  --

AndroidManifest_adobe.xml: {'BILLING', 'ACCESS_FINE_LOCATION', 'BLUETOOTH', 'WRITE', 'BIND_GET_INSTALL_REFERRER_SERVICE', 'WAKE_LOCK', 'RECEIVE', 'ACCESS_WIFI_STATE', 'READ_PHONE_STATE', 'ACCESS_NETWORK_STATE', 'RECORD_AUDIO', 'READ_CONTACTS', 'ACCESS_COARSE_LOCATION', 'FOREGROUND_SERVICE', 'READ_EXTERNAL_STORAGE', 'CAMERA', 'MODIFY_AUDIO_SETTINGS', 'READ', 'INTERNET', 'WRITE_EXTERNAL_STORAGE'}

AndroidManifest_asana.xml: {'VIBRATE', 'USE_CREDENTIALS', 'RECEIVE', 'WAKE_LOCK', 'ACCESS_NETWORK_STATE', 'INTERNET', 'READ_CONTACTS', 'RECEIVE_BOOT_COMPLETED', 'READ_EXTERNAL_STORAGE', 'BIND_GET_INSTALL_REFERRER_SERVICE', 'WRITE_EXTERNAL_STORAGE', 'GET_ACCOUNTS'}

AndroidManifest_blizzard.xml: {'VIBRATE', 'WAKE_LOCK', 'RECEIVE', 'REQUEST_INSTALL_PACKAGES', 'ACCESS_FINE_LOCATION', 'ACCESS_WIFI_STATE', 'C2D_MESSAGE', 'ACCESS_NETWORK_STATE', 'INTERNET', 'RECEIVE_BOOT_COMPLETED', 'READ_EXTERNAL_STORAGE', 'WRITE_EXTERNAL_STORAGE', 'CHANGE_WIFI_STATE'}

AndroidManifest_chess.xml: {'VIBRATE', 'WAKE_LOCK', 'RECEIVE', 'BILLING', 'ACCESS_COARSE_LOCATION', 'ACCESS_WIFI_STATE', 'ACCESS_NETWORK_STATE', 'FOREGROUND_SERVICE', 'INTERNET', 'READ_CONTACTS', 'RECEIVE_BOOT_COMPLETED', 'READ_EXTERNAL_STORAGE', 'BIND_GET_INSTALL_REFERRER_SERVICE', 'CAMERA', 'WRITE_EXTERNAL_STORAGE'}

AndroidManifest_clover.xml: {'BILLING', 'ACCESS_FINE_LOCATION', 'BLUETOOTH', 'WRITE', 'BIND_GET_INSTALL_REFERRER_SERVICE', 'WAKE_LOCK', 'RECEIVE', 'ACCESS_WIFI_STATE', 'READ_PHONE_STATE', 'ACCESS_NETWORK_STATE', 'RECORD_AUDIO', 'READ_CONTACTS', 'ACCESS_COARSE_LOCATION', 'FOREGROUND_SERVICE', 'READ_EXTERNAL_STORAGE', 'CAMERA', 'MODIFY_AUDIO_SETTINGS', 'READ', 'INTERNET', 'WRITE_EXTERNAL_STORAGE'}

AndroidManifest_copilot.xml: {'WAKE_LOCK', 'REQUEST_INSTALL_PACKAGES', 'RECEIVE', 'MODIFY_AUDIO_SETTINGS', 'CAMERA', 'CHECK_LICENSE', 'BILLING', 'ACCESS_FINE_LOCATION', 'ACCESS_WIFI_STATE', 'READ_PHONE_STATE', 'ACCESS_BACKGROUND_LOCATION', 'ACCESS_NETWORK_STATE', 'DOWNLOAD_WITHOUT_NOTIFICATION', 'FOREGROUND_SERVICE', 'INTERNET', 'READ_CONTACTS', 'BIND_GET_INSTALL_REFERRER_SERVICE', 'WRITE_EXTERNAL_STORAGE'}

AndroidManifest_duolingo.xml: {'RECEIVE', 'WAKE_LOCK', 'BILLING', 'READ_PHONE_STATE', 'C2D_MESSAGE', 'ACCESS_NETWORK_STATE', 'RECORD_AUDIO', 'INTERNET', 'BACKGROUND_FILE_UPLOAD', 'CAMERA', 'GET_ACCOUNTS', 'WRITE_EXTERNAL_STORAGE'}

AndroidManifest_endlessReader.xml: {'WAKE_LOCK', 'CHECK_LICENSE', 'BILLING', 'ACCESS_WIFI_STATE', 'ACCESS_NETWORK_STATE', 'INTERNET', 'WRITE_EXTERNAL_STORAGE'}

AndroidManifest_smarttrainer.xml: {'VIBRATE', 'NFC', 'BLUETOOTH_PRIVILEGED', 'READ_EXTERNAL_STORAGE', 'READ_GSERVICES', 'ACCESS_WIFI_STATE', 'ACCESS_FINE_LOCATION', 'READ_PHONE_STATE', 'ACCESS_COARSE_LOCATION', 'ACCESS_NETWORK_STATE', 'INTERNET', 'RECEIVE_BOOT_COMPLETED', 'BLUETOOTH_ADMIN', 'BLUETOOTH', 'WRITE_EXTERNAL_STORAGE'}

AndroidManifest_sony.xml: {'VIBRATE', 'WAKE_LOCK', 'RECEIVE', 'C2D_MESSAGE', 'ACCESS_NETWORK_STATE', 'INTERNET', 'BIND_GET_INSTALL_REFERRER_SERVICE', 'CAMERA'}


--                  --
--    PERMISSÕES    --
--      UNICAS      --
--     POR  APK     --
--                  --

AndroidManifest_asana.xml
         - USE_CREDENTIALS
AndroidManifest_blizzard.xml
         - CHANGE_WIFI_STATE
AndroidManifest_copilot.xml
         - DOWNLOAD_WITHOUT_NOTIFICATION
         - ACCESS_BACKGROUND_LOCATION
AndroidManifest_duolingo.xml
         - BACKGROUND_FILE_UPLOAD
AndroidManifest_smarttrainer.xml
         - BLUETOOTH_ADMIN
         - READ_GSERVICES
         - NFC
         - BLUETOOTH_PRIVILEGED

--                  --
--    PERMISSÕES    --
--      COMUNS      --
--     DAS  APK     --
--                  --

         - ACCESS_NETWORK_STATE
         - INTERNET