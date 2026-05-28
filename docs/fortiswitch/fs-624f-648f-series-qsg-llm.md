  FZATINET
  FortlSwltch 648F-FPOE
 FortiSwitch 624F/648F Series
FS-624F, FS-624F-FPOE, FS-648F, FS-648F-FPOE
                QuickStart Guide
---
                                                                                                                                                                                                                       Before you begin
                                                                                                                                                                                    Register your device to access FortiGuard updates, cloud management,
                                                                                                                                                                                    firmware upgrades, technical support and warranty coverage.
                                                                                                                                                                                                                          https://support.fortinet.com
August 21, 2024
This guide covers models: FS-624F, FS-624F-FPOE, FS-648F, FS-648F-FPOE
Copyright© 2023 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered
trademarks of Fortinet, Inc., in the U.S. and other jurisdictions, and other Fortinet names herein may also be registered and/or common law
trademarks of Fortinet. All other product or company names may be trademarks of their respective owners. Performance and other metrics
contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network
variables, different network environments and other conditions may affect performance results. Nothing herein represents any binding
commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding
written contract, signed   by Fortinet’s General Counsel, with a purchaser that expressly warrants that the identified product will perform
according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified
in such binding written contract shall be binding on Fortinet. For absolute clarity, any such warranty will be limited to performance in the same
ideal conditions as in Fortinet’s internal lab tests. In no event does Fortinet make any commitment related to future deliverables, features or
development, and circumstances may change such that any forward-looking statements herein are not accurate. Fortinet disclaims in full
any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify,
transfer, or otherwise revise this publication without notice, and the most current version of the publication shall be applicable.
For Product License Agreement / EULA and Warranty Terms, visit https://www.fortinet.com/content/dam/fortinet/assets/legal/EULA.pdf
---
                            The Essentials                                                                              Package Contents
   Default Logins                                                                                   FortiSwitch 624F/648F Series
                                                                                                    FS-624F, FS-624F-FPOE, FS-648F, FS-648F-FPOE
           https://192.168.1.99
           Username: admin
           Password: leave blank
                                                                                                                                             FE3:ATINET
                                                                                                                                         FortiSwitch 624F/648F Series
    Fortinet Documents Library                                                                                                           FS-624F,FS-624F-FPOE, FS-648F,FS-648F-FPOE
                                                                                                                                          QuickStart Guide
    For a detailed Administration Guide, up-to-date Hardware documentation and                               FortiSwitch Device           QuickStart Guide   1x Console Cable
    Reference Manuals, visit https://docs.fortinet.com/                                                                                                       (RJ45 to USB)
    Customer Service
    For contracts, licensing, product registration and account management,
    contact FortiCare Support at https://www.fortinet.com/support/contact                                                0_0₀
    Technical Support                                                                                      2x Rack Mount Brackets        2x Rails w/screws     4x Rubber Feet
                                                                                                           and 2x Rail Stoppers              (28x M4x5,
                                                                                                                                              2x M4x8)
    To access our Resource Center, Professional Services and Technical Support
    Services, visit https://www.fortinet.com/support
                           Thank you for choosing Fortinet
                                                                                                                                    2x AC Power Cables
4                                                                                                                                                                                    5
---
                            Setup Options
    Set up your Fortinet device locally or use cloud management mode.                               FortiLink
    GUI
                1                                     3     https://192.168.1.99
                                                            Username: admin
                                                             No Password
                                     2                                                                FortiSwitch Port                                            FortiGate Port
              MGMT                                                                                                                   Ethernet Cable
                                                     Management Computer
                                Ethernet Cable
      Note: For static IP configuration, use 192.168.1.1 with subnet mask                            1   Login to the FortiGate and go to WiFi & Switch Controller -> FortiLink Interface
      255.255.255.0                                                                                  2   Add a FortiGate Port in the FortiLink interface
                                                                                                     3   When the device is discovered, select Authorize
    CLI
                1                      2             3      Speed (default):  115200                  Optional: To automatically authorize the device upon discovery, enable
                                                            Data bits:      8                         “Automatically authorize devices” in the FortiLink Interface settings
                                                            Stop bits:      1
                                                            Parity:         None
                                 Console Cable              Flow Control:   None
           Console Port
                                                           Management Computer
      Note: For a detailed CLI guide, visit docs.fortinet.com
    Cloud Management               (Connect a port to the Internet)
    1  Visit support.fortinet.com to register your device and cloud management license
    2  Sign in at https://fortilan.forticloud.com to manage your Inventory List
6                                                                                                                                                                                    7
---
                             SFP Modules                                                                                   Rail Installation
    Installation
                                                                                                             3
                                                    Cage Socket                                       Secure Rail Stoppers                2
                                                                                                                                      Attach Rails                   1
                                           1                                                                                                               Install Rackmount Brackets
                             SFP
                  2   Tx
                             Rx                                                                     Rail Stopper Screws
                                                                                                    (2x M4x8 on each side)        28x M4x5 Screws
                                                                                                                                  (14 on each side)
    Removal
                                                    Cage Socket                                      Note: The recommended clearance is 1.5 inches above and below the
                                           1                                                         device.
                                 2                  Lock                                             Caution: To avoid personal injury or damage to the device, it is
                                                                                                     recommended that two or more people mount the device on a rack.
                        SFP
8                                                                                                                                                                                   9
---
                    Front FS-624F /-FPOE
                 8 1
                 3
                                                                                                              1                                         2         3       4
     1    Ports 1 to 24 (RJ45)                                                                       3    PWR1
            Green: Link established at 5Gbps                                                                 Green: Power is on
            Flashing Green: 5Gbps data activity                                                              Amber: PSU detected, but no AC power
            Blue: Link established at 2.5Gbps                                                                Off: PSU removed
            Flashing Blue: 2.5Gbps data activity                                                          PWR2
            Amber: Link established at 1000/100/10Mbps                                                       Green: Power is on
            Flashing Amber: 1000/100/10Mbps data activity                                                    Amber: PSU detected, but no AC power
            Off: No link established                                                                         Off: PSU removed
          POE Ports 1 to 24 (RJ45) FPOE models only                                                       ALARM
            Amber: Powering a device                                                                         Amber: Alarm detected
            Off: Not powering a device                                                                       Off: No alarm detected
     2    Ports 25 to 28 (SFP28)                                                                          FAN
            Green: Link established at 25Gbps                                                                Green: Fan operating normally
            Flashing Green: Data activity                                                                    Amber: Fan alarm detected
             Amber: Link established at 10Gbps                                                               Off: Fan is off
             Flashing Amber: Data activity                                                                PoE Max (up to 1440W) FPOE models only
            Off: No link established                                                                         Amber: Providing Max PoE power
                                                                                                             Off: PoE power available
      Note: For FPOE models, the default port LED indicates port activity. Use
      the CLI to set port-led-mode to PoE to indicate the port PoE status.                           4     MGMT (RJ45) default IP 192.168.1.99
                                                                                                             Green: Link established                                    Link/Activity
                                                                                                             Flashing Green: Data activity
                                                                                                             Off: No link established                           MGMT Port
                                                                                                           USB (USB A) USB 2.0 server port
                                                                                                           Console (RJ45) CLI management port
10                                                                                                                                                                                   11
---
                  Rear FS-624F /-FPOE
           IPPS IN IPPS OUT
             1                                                                                                                        2
       1    1PPS IN/OUT (SMB) Pulse per second synchronization ports
       2    Redundant Power Supplies (System Rated per PSU)
            FS-624F: 100-240VAC, 3A Max, 50-60Hz
            FS-624F-FPOE: 100-127VAC, 12A Max or 200-240VAC, 6A Max, 50-60Hz
12                                                                                                                                                                13
---
                    Front FS-648F /-FPOE
                 H
                 8
                                                   1                                                                     2                                   3      4        5
     1    Ports 1 to 32 (RJ45)                                                                       4    PWR1
             Green: Link established at 2.5Gbps                                                              Green: Power is on
             Flashing Green:2.5Gbps data activity                                                            Amber: PSU detected, but no AC power
             Amber: Link established at 1000/100/10Mbps                                                      Off: PSU removed
             Flashing Amber: 1000/100/10Mbps data activity                                                PWR2
             Off: No link established                                                                        Green: Power is on
     2    Ports 33 to 48 (RJ45)                                                                              Amber: PSU detected, but no AC power
                                                                                                             Off: PSU removed
             Green: Link established at 5Gbps
             Flashing Green: 5Gbps data activity                                                          ALARM
             Blue: Link established at 2.5Gbps                                                               Amber: Alarm detected
             Flashing Blue: 2.5Gbps data activity                                                            Off: No alarm detected
             Amber: Link established at 1000/100/10Mbps
             Flashing Amber: 1000/100/10Mbps data activity                                                FAN
             Off: No link established                                                                        Green: Fan operating normally
         POE Ports 1 to 48 (RJ45) FPOE models only                                                           Amber: Fan alarm detected
                                                                                                             Off: Fan is off
            Amber: Powering a device
            Off: Not powering a device                                                                    PoE Max (up to 1800W) FPOE models only
                                                                                                             Amber: Providing Max PoE power
     3    Ports 49 to 56 (SFP28)                                                                             Off: PoE power available
             Green: Link established at 25Gbps
             Flashing Green: Data activity                                                           5     MGMT (RJ45) default IP 192.168.1.99
             Amber: Link established at 10Gbps                                                               Green: Link established                                    Link/Activity
             Flashing Amber: Data activity                                                                   Flashing Green: Data activity
             Off: No link established                                                                        Off: No link established                           MGMT Port
                                                                                                           USB (USB A) USB 2.0 server port
      Note: For FPOE models, the default port LED indicates port activity. Use                             Console (RJ45) CLI management port
      the CLI to set port-led-mode to PoE to indicate the port PoE status.
14                                                                                                                                                                                   15
    8
---
                  Rear FS-648F /-FPOE
           IPPS IN 1PPS OUT
             1                                                                                                                          2
       1    1PPS IN/OUT (SMB) Pulse per second synchronization ports
       2    Redundant Power Supplies (System Rated per PSU)
            FS-648F: 100-240VAC, 3A Max, 50-60Hz
            FS-648F-FPOE: 100-127VAC, 12A Max or 200-240VAC, 6A Max, 50-60Hz
16                                                                                                                                                                   17
---
       Cautions and Warnings                                                                                                                                                                                      The rack may tip over causing serious personal injury.
                                                                                                                                                                                                                  O rack pode tombar causando ferimentos graves.
       Environmental speciﬁcations                                                                                                                                                                                Before extending the rack to the installation position, read the installation instructions.
                                                                                                                                                                                                                  Antes de estender o rack para a posição de instalação, leia as instruções de instalação.
       Ambient operating temperature: 0°C to 45°C
       Rack Mount Instructions - The following or similar rack-mount instructions are included with the installation instructions:                                                                                Do not put any load on the slide-rail mounted equipment in the installation position.
                                                                                                                                                                                                                  Não coloque nenhuma carga no equipamento montado em trilho deslizante na posição de instalação.
       Instructions de montage en rack - Les instructions de montage en rack suivantes ou similaires sont incluses avec les instructions d’installation:                                                          Do not leave the slide-rail mounted equipment in the installation position.
       Elevated Operating Ambient - If installed in a closed or multi-unit rack assembly, the operating ambient temperature of the rack environment may be greater than                                           Não deixe o equipamento montado em trilho deslizante na posição de instalação.
       room ambient. Therefore, consideration should be given to installing the equipment in an environment compatible with the maximum ambient temperature (Tma)                                                 Laser Class 1 optical transceiver shall be used only
       specified by the manufacturer.                                                                                                                                                                             L’émetteur-récepteur optique de classe 1 laser doit être utilisé uniquement
       Température ambiante élevée – S’il est installé dans un rack fermé ou à unités multiples, la température ambiante de fonctionnement de l’environnement du rack
       peut être supérieure à la température ambiante de la pièce. Par conséquent, il est important d’installer le matériel dans un environnement respectant la température                                       IEC 60825-1:2014 transfer to FDA/CDRH Complies with FDA performance standards for laser products except for conformance with IEC 60825-1 Ed.3., as described
       ambiante maximale (Tma) stipulée par le fabricant.                                                                                                                                                         in Laser Notice No. 56, dated May 8, 2019.
       Reduced Air Flow - Installation of the equipment in a rack should be such that the amount of air flow required for safe operation of the equipment is not compromised.                                     IEC 60825-1:2014 transfert à la FDA/CDRH Conforme aux normes de performance de la FDA pour les produits laser, à l’exception de la conformité à la norme IEC
       Ventilation réduite – Installation de l’équipement dans un rack doit être telle que la quantité de flux d’air nécessaire au bon fonctionnement de l’équipement n’est pas                                   60825-1 Ed.3., comme décrit dans l’avis laser n° 56, daté du 8 mai 2019.
       compromise.
       Mechanical Loading - Mounting of the equipment in the rack should be such that a hazardous condition is not achieved due to uneven mechanical loading.                                                     The SFP ports should use UL Listed Optional Transceiver product, Rated 3.3Vdc, Laser Class 1.
       Chargement Mécanique – Montage de l’équipement dans le rack doit être telle qu’une situation dangereuse n’est pas lié à un chargement mécanique inégal.                                                    Les ports SFP doivent utiliser un produit émetteur-récepteur en option répertorié UL, 3,3 Vdc, classe laser 1.
       Circuit Overloading - Consideration should be given to the connection of the equipment to the supply circuit and the effect that overloading of the circuits might have                                    Fiber optic transceiver must be rated 3.3V, 22mA max, Laser Class 1, UL certified component.
       on overcurrent protection and supply wiring. Appropriate consideration of equipment nameplate ratings should be used when addressing this concern.                                                         Le transceiver optique doit avoir les valeurs nominales de 3.3 V, maximum 22 mA, Laser Class 1, homologué UL
       Surtension – Il convient de prendre l’ensemble des précautions nécessaires lors du branchement de l’équipement au circuit d’alimentation et être particulièrement                                          This product is intended to be supplied by means of a power cord connected to a socket-outlet with earthing connection.
       attentif aux effets de la suralimentation sur le dispositif assurant une protection contre les courts-circuits et le câblage. Ainsi, il est recommandé de tenir compte du                                  Ce produit est destiné à être alimenté au moyen d’un cordon d’alimentation relié à une prise de courant avec mise à la terre.
       numéro d’identification de l’équipement.
       Reliable Earthing - Reliable earthing of rack-mounted equipment should be maintained. Particular attention should be given to supply connections other than direct                                         Warning: Class I Equipment. This equipment must be earthed. The power plug must be connected to a properly wired earth ground socket outlet. An improperly wired
       connections to the branch circuit (e.g. use of power strips).                                                                                                                                              socket outlet could place hazardous voltage on accessible metal parts.
       Fiabilité de la mise à la terre – Fiabilité de la mise à la terre de l’équipement monté en rack doit être maintenue. Une attention particulière devrait être accordée aux                                  Avertissement: Équipement de classe I. Cet équipement doit être mis à la terre. La fiche d’alimentation doit être connectée à une prise de terre correctement câblée.
       connexions d’alimentation autres que les connexions directes au circuit de dérivation (par exemple de l’utilisation de bandes de puissance).                                                               Une prise de courant mal câblée pourrait placer une tension dangereuse sur les pièces métalliques accessibles.
       Refer to speciﬁc Product Model Data Sheet for Environmental Speciﬁcations (Operating Temperature‚ Storage Temperature‚ Humidity‚ and Altitude)                                                             Warning: All Ethernet cables are designed for intra-building connection to other equipment. Do not connect these ports directly to communication wiring or other wiring
                                                                                                                                                                                                                  that exits the building where the appliance is located.
       Référez à la Fiche Technique de ce produit pour les caractéristiques environnementales (Température de fonctionnement‚ température de stockage‚ humidité et                                                Avertissement: Tous les câbles Ethernet sont conçus pour une connexion intra-bâtiment à d’autres équipements. Ne connectez pas ces ports directement au câblage
       l’altitude).                                                                                                                                                                                               de communication ou à tout autre câblage qui sort du bâtiment où se trouve l’appareil.
       Safety
       Battery  – Risk of explosion if the battery is replaced by an incorrect type. Do not dispose of batteries in a fire. They may explode. Dispose of used batteries according
       to your local regulations. IMPORTANT: Switzerland: Annex 4.10 of SR814.013 applies to batteries.
       Batterie – Risque d’explosion si la batterie est remplacée par un type incorrect. Ne jetez pas les batteries au feu. Ils peuvent exploser. Jetez les piles usagées
       conformément aux réglementations locales. IMPORTANT: Suisse: l’annexe 4.10 de SR814.013 s’appliquent aux batteries.
       警告
       本電池如果更換不正確會有爆炸的危險
       請依製造商說明書處理用過之電池
       CAUTION:
       There is a danger of explosion if a battery is incorrect replaced. Replace only with the same or equivalent type.
       Dispose batteries of according to the manufacturer’s instructions.
       Disposing a battery into fire, a hot oven, mechanically crushing, or cutting it can result in an explosion.
       Leaving a battery in an extremely hot environment can result in leakage of flammable liquid, gas, or an explosion.
       If a battery is subjected to extremely low air pressure, it may result in leakage of flammable liquid, gas, or an explosion.
       WARNUNG:
       Lithium-Batterie Achtung: Explosionsgefahr bei fehlerhafter Batteriewechsel. Ersetzen Sie nur den gleichen oder gleichwertigen Typ. Batterien gemäß den Anweisungen
       des Herstellers entsorgen.
       Beseitigung einer BATTERIE in Feuer oder einen heißen Ofen oder mechanisches Zerkleinern oder Schneiden einer BATTERIE, die zu einer EXPLOSION führen kann
       Verlassen einer BATTERIE in einer extrem hohen Umgebungstemperatur, die zu einer EXPLOSION oder zum Austreten von brennbarer Flüssigkeit oder Gas führen kann
       Eine BATTERIE, die einem extrem niedrigen Luftdruck ausgesetzt ist, der zu einer EXPLOSION oder zum Austreten von brennbarer Flüssigkeit oder Gas führen kann.
       Caution: This equipment is to be used in a Network Environment 0 per IECTR 62101.  This product is connected only to PoE networks without routing to the outside
       plant.
       Attention: Ce matériel doit être utilisé dans un Environnement Réseau 0 par IECTR 62101. Ce produit est uniquement connecté aux réseaux PoE sans installation
       externe de routage.
       CAUTION: Shock Hazard. Disconnect all power sources.
       ATTENTION: Risque d’électrocution. Débranchez toutes les sources d’alimentation.
       Grounding — To prevent damage to your equipment, connections that enter from outside the building should pass through a lightning / surge protector, and be
       properly grounded. Use an electrostatic discharge workstation (ESD) and/or wear an anti-static wrist strap while you work. In addition to the grounding terminal of the
       plug, on the back panel, there is another, separate terminal for earthing.
       Mise à la terre — Pour éviter d’endommager votre matériel, assurez-vous que les branchements qui entrent à partir de l’extérieur du bâtiment passent par un
       parafoudre / parasurtenseur et sont correctement mis à la terre. Utilisez un poste de travail de décharge électrostatique (ESD) et / ou portez un bracelet anti-statique
       lorsque vous travaillez. Ce produit possède une borne de mise à la terre qui est prévu à l’arrière du produit, à ceci s’ajoute la mise à la terre de la prise.
       This product has a separate protective earthing terminal provided on the back of the product in addition to the grounding terminal of the attachment plug.  This
       separate protective earthing terminal must be permanently connected to earth with a green with yellow stripe conductor minimum size # 14 AWG and the connection is
       to be installed by a qualified service personnel.
       Ce produit a une borne de mise à la terre séparé sur le dos de l’appareil, en plus de la borne de mise à la terre de la fiche de raccordement. Cette borne de mise à la
       terre séparée doit être connecté en permanence à la terre avec un conducteur vert avec la taille bande jaune de minimum # 14 AWG et la connexion doit être installé
       par un personnel qualifié.
       Caution: Slide/rail mounted equipment is not to be used as a shelf or a work space.
       Attention: Un équipement monté sur bâti ne doit pas être utilisé sur une étagère ou dans un espace de travail.
       Warning: Stability hazard.
       Aviso: Perigo de estabilidade.
18                                                                                                                                                                                                                                                                                                                                                                                          19
---
      Regulatory Notices
      Federal Communication Commission (FCC) – USA
      This device complies with Part 15 of the FCC Rules.  Operation is subject to the following two conditions:
      (1) this device may not cause harmful interference, and
      (2) this device must accept any interference received; including interference that may cause undesired operation.
      This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules.  These limits are designed to
      provide reasonable protection against harmful interference when the equipment is operated in a commercial environment.  This equipment generates, uses, and can
      radiate radio frequency energy, and if it is not installed and used in accordance with the instruction manual, it may cause harmful interference to radio communications.
      Operation of this equipment in a residential area is likely to cause harmful interference, in which case the user will be required to correct the interference at his own
      expense.
      WARNING: Any changes or modifications to this product not expressly approved by the party responsible for compliance could void the user’s authority to operate the
      equipment
      Industry Canada Equipment Standard for Digital Equipment (ICES) – Canada
      CAN ICES-003 (A) / NMB-003 (A)
      This digital apparatus does not exceed the Class A limits for radio noise emissions from digital apparatus set out in the Radio Interference Regulations of the Canadian
      Department of Communications.
      Cet appareil numérique n’émet pas de bruits radioélectriques dépassant les limites applicables aux appareils numériques de la classe A prescrites dans le Règlement
      sur le brouillage radioélectrique édicte par le ministère des Communications du Canada.
      European Conformity (CE) - EU
      This is a Class A product. In a domestic environment, this product may cause radio interference, in which case the user may be required to take adequate measures.
      C€
      Voluntary Control Council for Interference (VCCI) – Japan
      この装置は、クラスＡ機器です。この装置を住宅環境で使用すると電波妨害を引き起こすことがあります。この場合には使用者が適切な対策を講ずるよう要求
      されることがあります。
                                                                                                                                   ＶＣＣＩ－Ａ
      Product Safety Electrical Appliance & Material (PSE) – Japan
      日本では電気用品安全法(PSE)の規定により、同梱している電源コードは本製品の専用電源コードとして利用し、他の製品に使用しないでください。
      Bureau of Standards Metrology and Inspection (BSMI) – Taiwan
      The presence conditions of the restricted substance (BSMI RoHS table) are available at the link below:
      限用物質含有情況表 (RoHS Table) 請到以下 網址下載：
      https://www.fortinet.com/bsmi
      警告： 為避免電磁干擾，本產品不應安裝或使用於住宅環境。
      請仔細閱讀以下說明
      本設備勿置於潮濕處。
      連接至電源前，請先檢查電壓。
      當設備不用時，請將所有電源線拔除，避免電壓不穩而造成傷害。
      勿將任何液體濺入設備中，避免線路短路。
      基於安全理由，只有受到專業訓練的從業人員，才可以打開本設備。
      請勿自行調整或修理已通電的設備，以確保您的安全。
      如不小心受傷，請立刻找急救人員給予您適當的救護，千萬別因傷勢輕微而忽略自己的傷勢。
      請依照台灣法規處置電池。
      若不正確替換電池可能導致爆炸危險，替換電池時，請使用設備生產商推薦使用的電池。
      請勿拆卸、刺穿或以其他方式損壞電池。
      雷射設備非用戶維修設備，請與生產商聯繫維修事宜。
      注意: 要斷開電源，請將所有電源線從本機上拔下
      英屬蓋曼群島商防特網股份有限公司台灣分公司
      地址：台北市內湖區行愛路176號2樓
      電話：(02) 27961666
      China
      警告: 在居住环境中，运行此设备可能会造成无线电干扰。
      For models FS-624F-FPOE and FS-648F-FPOE
      Agência Nacional de Telecomunicações (ANATEL) – Brazil
      CISPR 22
      Este produto não é apropriado para uso em ambientes domésticos, pois poderá causar interferências eletromagnéticas que obrigam o usuário a tomar medidas
      necessárias para minimizar estas interferências.
20                                                                                                                                                                                                                                                                                                                       21
---
22                                                                                                                                                                   23
---
Fortinet.com