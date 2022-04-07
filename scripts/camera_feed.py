# importing libraries
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as img

x_path=[2026.6670000000001, 2026.6665933555237, 2026.6691968861007, 2026.6916907897012, 2026.7639182850287, 2026.9264518710545, 2027.2285203917772, 2027.726092030674, 2028.4801083593009, 2029.554864564508, 2031.0165309787267, 2032.9318110377903, 2035.3667307907583, 2038.3855550861927, 2042.0498255593575, 2046.4175155447997, 2051.542297038774, 2057.4729148359743, 2064.252662965022, 2071.9189585472, 2080.5030082028584, 2090.0295621299833, 2100.516750979373, 2111.976000650888, 2124.4120201352434, 2137.8228575257904, 2152.200019324759, 2167.528648168429, 2183.787754095671, 2200.95049448434, 2218.9844977799717, 2237.852226141244, 2257.51137212667, 2277.915284546977, 2299.0134186076434, 2320.751805466041, 2343.0735363276576, 2365.919256205854, 2389.2276624696196, 2412.936003303784, 2436.980571206158, 2461.297186646045, 2485.8216670086044, 2510.4902759495253, 2535.2401482844534, 2560.0096855376614, 2584.7389172743933, 2609.369823341387, 2633.8466121399756, 2658.1159500562935, 2682.127137173007, 2705.8322243870352, 2729.186067057749, 2752.1463103100855, 2774.673301117017, 2796.7299222859237, 2818.281343473207, 2839.2946843517257, 2859.738585055411, 2879.582679025634, 2898.7969633836433, 2900.000000000048, 2918.5249248895248, 2936.438109104625, 2953.7832501854464, 2970.596465205229, 2986.9059600107503, 3002.731785330803, 3018.085685142817, 3032.971042687025, 3047.3829295181386, 3061.3082629844503, 3074.7260775238374, 3087.6079151666763, 3099.918340635464, 3111.6155864306947, 3122.6523332930738, 3132.976631431604, 3142.5329679074166, 3149.9999999922857, 3157.9990214757077, 3165.1581822291073, 3171.514049390459, 3177.103799618308, 3181.9651130619823, 3186.1360674264824, 3189.6550323258593, 3192.560564118785, 3194.891301420288, 3196.685861483252, 3197.982737643658, 3198.8201980232607, 3199.236185683466, 3199.2682204243897, 3198.953302422648, 3198.3278179018976, 3197.4274470297873, 3196.2870742351674, 3194.9407011393773, 3193.4213622953657, 3191.761043928456, 3189.990605872602, 3188.1397068958513, 3186.23673360887, 3184.308733150364, 3182.381349843051, 3180.4787660141837, 3178.623647174254, 3176.8370917477596, 3175.138585549804, 3173.5459612023897, 3172.0753626840205, 3170.741215206851, 3169.5562006143973, 3168.5312384945573, 3167.6754732009704, 3166.9962669769666, 3166.4991993756394, 3166.1880731700894, 3166.064926947385, 3166.1300545802023, 3166.3820317698774, 3166.8177498547648, 3167.432457077597, 3168.2198075054184, 3169.1719177967425, 3170.2794320084868, 3171.531594637574, 3172.9163320902917, 3174.4203427737375, 3176.029196002619, 3177.7274399157104, 3179.498718595285, 3181.32589858388, 3183.191204991632, 3185.0763673882248, 3186.962775673419, 3188.8316461199574, 3190.664197781851, 3192.441839463063, 3194.146367439702, 3195.7601741294784, 3197.2664679024892, 3198.6495042268143, 3199.894828343604, 3200.000000000453, 3201.084061386523, 3202.025940673225, 3202.8351056117526, 3203.520789594757, 3204.0919815589377, 3204.5574163967267, 3204.925565893972, 3205.2046302102617, 3205.402529918917, 3205.526898623213, 3205.585076165821, 3205.5841024482243, 3205.530711876765, 3205.4313284524032, 3205.2920615207677, 3205.1187021993774, 3204.916720498808, 3204.69126315468, 3204.447152187171, 3204.1888842050193, 3203.9206304705276, 3203.6462377426615, 3203.369229915046, 3203.092810465263, 3202.819865732841, 3202.5529690422372, 3202.2943856880192, 3202.046078798581, 3201.8097160958023, 3201.5866775667073, 3201.378064064864, 3201.184706857217, 3201.007178134205, 3200.845802499327, 3200.7006694551055, 3200.5716469022846, 3200.458395669084, 3200.360385087468, 3200.2769096326556, 3200.2071066434182, 3200.149975139604, 3200.104395753431, 3200.0691517919404, 3200.042951447016, 3200.024451169673, 3200.012280226103, 3200.005066451082, 3200.0014632168786, 3200.0001776334393, 3199.999999997388]
y_path=[3499.999999999999, 3500.000659348177, 3500.0007195796934, 3499.9879385288173, 3499.939089790221, 3499.821737188759, 3499.595887144012, 3499.2155225042648, 3498.630021424631, 3497.7854648640364, 3496.6258362757176, 3495.0941170659867, 3493.13328139591, 3490.6871939006373, 3487.7014139010566, 3484.1239096824775, 3479.9056864150475, 3475.0013312905917, 3469.369479450575, 3462.9732042798846, 3455.78033564114, 3447.763709624212, 3438.901353385652, 3429.17660865275, 3418.578197466887, 3407.100233740906, 3394.742184205185, 3381.5087823171116, 3367.4098987086622, 3352.4603717467876, 3336.679801781277, 3320.0923126548378, 3302.7262840500553, 3284.6140582479516, 3265.7916248728216, 3246.298287198068, 3226.1763135877154, 3205.4705776482983, 3184.2281906658473, 3162.498129902634, 3140.330866328402, 3117.777995360766, 3094.89187418949, 3071.725269259321, 3048.3310174861044, 3024.761704780849, 3001.069365456465, 2977.305206091863, 2953.5193574280956, 2929.760657871274, 2906.076472176929, 2882.512548890518, 2859.112920118795, 2835.9198472067064, 2812.973815894563, 2790.3135845301194, 2767.976288910314, 2745.99760732735, 2724.4119893938023, 2703.252952221448, 2682.5534475285713, 2681.2499999994006, 2661.095373161552, 2641.580897642789, 2622.8316337182714, 2604.9492958365845, 2588.011561501291, 2572.0716012046105, 2557.157842193821, 2543.273978850757, 2530.3992424651697, 2518.4889431820047, 2507.4752969038855, 2497.268549928329, 2487.7584141012267, 2478.8158252662397, 2470.295037791162, 2462.0360679516816, 2453.8674989527935, 2446.869999997907, 2438.4300453311535, 2429.7883380452995, 2420.988065971126, 2412.0717106055936, 2403.080960149497, 2394.056624041229, 2385.0385491411034, 2376.0655377206385, 2367.1752674113122, 2358.404213267166, 2349.787572095736, 2341.3591892117447, 2333.151487767995, 2325.1954008179173, 2317.5203062641804, 2310.1539648478793, 2303.122461332646, 2296.450149038198, 2290.1595978777755, 2284.2715460538025, 2278.8048555664022, 2273.7764716889637, 2269.201386565473, 2265.0926070838195, 2261.461127179638, 2258.3159047251693, 2255.6638431574065, 2253.509778000176, 2251.85646843447, 2250.7045940715134, 2250.0527570829618, 2249.8974898427614, 2250.2332682350725, 2251.052530782583, 2252.345703749953, 2254.101232376387, 2256.3056183923127, 2258.9434639740557, 2261.9975222914254, 2265.4487548023862, 2269.276395449291, 2273.4580219111285, 2277.9696340664013, 2282.7857398207634, 2287.879448454034, 2293.2225716411667, 2298.7857323013213, 2304.5384814296285, 2310.4494230661785, 2316.4863475565835, 2322.616373258428, 2328.806096848315, 2335.0217523838437, 2341.229379274686, 2347.394999317843, 2353.4848029507702, 2359.4653448773097, 2365.3037492210387, 2370.967924359542, 2376.426787595152, 2381.650499816202, 2386.61071030279, 2391.2808118320972, 2395.6362062375265, 2399.654580576098, 2399.9999999979427, 2403.633291405545, 2406.919200364535, 2409.869311910821, 2412.4955432656106, 2414.8101241092336, 2416.8255758281275, 2418.554689718894, 2420.0105041338347, 2421.2062805521837, 2422.155478561186, 2422.8717297313706, 2423.368810370098, 2423.660613137805, 2423.7611175109787, 2423.684359076241, 2423.4443976397106, 2423.0552841358694, 2422.531026320179, 2421.885553229691, 2421.132678395854, 2420.2860617937604, 2419.3591705121344, 2418.365238128048, 2417.3172227710184, 2416.2277638602227, 2415.109137499554, 2413.973210514301, 2412.831393114002, 2411.6945901655236, 2410.5731510607693, 2409.4768181630243, 2408.414673816349, 2407.395085902157, 2406.425651927293, 2405.5131416277145, 2404.66343807217, 2403.881477249932, 2403.1711861269614, 2402.5354191546685, 2401.975893215491, 2401.4931209895003, 2401.0863427264485, 2400.753456407172, 2400.4909462788564, 2400.29380974824, 2400.1554826170577, 2400.067762644103, 2400.020731417513, 2400.002674522544, 2399.9999999881]
z_path=[2500.0000000000005, 2500.0021022163683, 2500.0173904237877, 2500.060298982519, 2500.1460028737365, 2500.2897986128773, 2500.5065531523246, 2500.810218182409, 2501.213407239676, 2501.727033031418, 2502.36000238541, 2503.118966233841, 2504.0081220404054, 2505.0290660795195, 2506.1806929766385, 2507.4591399186447, 2508.857772943269, 2510.367212716526, 2511.975397207123, 2513.6676786668263, 2515.4269523257326, 2517.2338142114468, 2519.0667455011007, 2520.9023208152153, 2522.71543786235, 2524.47956584353, 2526.167010025406, 2527.7491898911285, 2529.1969282778937, 2530.480748910142, 2531.571179737383, 2532.439059485591, 2533.055844831175, 2533.393915606477, 2533.426875445756, 2533.1298452806564, 2532.479747094105, 2531.455575341622, 2530.0386534490076, 2528.2128727953786, 2525.964911590526, 2523.2844310555597, 2520.1642463158073, 2516.6004694149547, 2512.592621859369, 2508.143714101603, 2503.260289372034, 2497.952429267608, 2492.233718506671, 2486.1211662588444, 2479.6350814589136, 2472.798899513719, 2465.6389578109906, 2458.1842174391263, 2450.4659285268563, 2442.517236611786, 2434.37272744677, 2426.0679076531032, 2417.638618629482, 2409.120381125721, 2400.5476678901855, 2400.000000000363, 2391.4207049672586, 2382.9414176074342, 2374.668635874791, 2366.693848979564, 2359.0929150974334, 2351.9255859581335, 2345.2351873111365, 2339.0484642658757, 2333.375600504194, 2328.210420362304, 2323.5307827800134, 2319.2991761146404, 2315.4635228171683, 2311.958202968086, 2308.70530567057, 2305.6161172987013, 2302.5928555974388, 2300.000000010845, 2296.835034559158, 2293.523820110725, 2290.0504722502465, 2286.397819748484, 2282.547490462859, 2278.479998908685, 2274.1748354017186, 2269.610556672882, 2264.7648778558164, 2259.6147657480874, 2254.136533246768, 2248.3059348591637, 2242.098263189457, 2235.488446301972, 2228.4511458619027, 2220.960855954151, 2212.99200248114, 2204.5190430402827, 2195.5165671819036, 2185.9593969483285, 2175.822687594978, 2165.0820283941007, 2153.7135434220345, 2141.6939922306547, 2129.000870303781, 2115.612509199376, 2101.5081762781892, 2086.668173919632, 2071.0739381257354, 2054.708136413748, 2037.554764898386, 2019.5992444642152, 2000.8285159291772, 1981.2311340998594, 1960.7973606192518, 1939.519255507911, 1917.39076729906, 1894.4078216686203, 1870.5684084607628, 1845.872667009613, 1820.3229696583985, 1793.9240033761234, 1766.6828493729154, 1738.6090606147945, 1709.7147371385254, 1680.0145990672172, 1649.5260572276948, 1618.2692812702044, 1586.2672651911344, 1553.5458901598595, 1520.1339845498878, 1486.0633810758245, 1451.3689709361752, 1416.0887548630944, 1380.2638909800426, 1343.9387393675352, 1307.1609032384622, 1269.9812666227372, 1232.4540284634859, 1194.6367330239918, 1156.59029650706, 1118.3790297875603, 1080.0706571582596, 1041.7363309907087, 1003.450642210657, 999.9999999975898, 961.8512482105689, 923.8862196074278, 886.1548818694882, 848.7069530384524, 811.5918121872764, 774.858407189331, 738.5551595445231, 702.7298662213398, 667.4295984735618, 632.7005975900265, 598.5881675368073, 565.1365644494872, 532.3888829360221, 500.38693914662144, 469.1711505716048, 438.7804125244984, 409.2519712696303, 380.6212937531891, 352.9219338958137, 326.18539540634447, 300.44099107450165, 275.71569850214655, 252.03401223114633, 229.4177922270028, 207.8861086768993, 187.45508306056217, 168.13772545359097, 149.94376802055922, 132.87949465801648, 116.94756674550445, 102.14684496302652, 88.47220713448769, 75.914362055104, 64.45965926185454, 54.08989470599772, 44.78211228556029, 36.50840119745408, 29.23568906744913, 22.925530816799437, 17.533893224375788, 13.010935142716335, 9.300783327809768, 6.341303839290049, 4.063868971948978, 2.39311967616959, 1.246723426054814, 0.5351274945423938, 0.1613075932546053, 0.02051183690491598, -9.575160220265388e-09]
img2 = img.imread('database_img.png') # trainImage
capture_resolution= [341,426]    #[120,160] 

fig = plt.figure(figsize=(8,8))
viewer = fig.add_subplot(111)
plt.ion() # Turns interactive mode on (probably unnecessary)
fig.show() # Initially shows the figure

plt.title("Camera input", fontsize=20)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
res=  500      #118.45
f=1000/1000
# Loop
for i in range(len(x_path)):
    y_true,x_true= y_path[i], x_path[i]
    capture_resolution=[((z_path[i]+200)/res)*256*(1/f),((z_path[i]+200)/res)*320*(1/f)]                            #[0.577*k1*(z_path[i]+10),0.577*k2*(z_path[i]+10)]
    img1 = img2[int(round(y_true-capture_resolution[0]/2)):int(round(y_true+capture_resolution[0]/2)),int(round( x_true-capture_resolution[1]/2)):int(round(x_true+capture_resolution[1]/2))]
    viewer.clear() # Clears the previous image
    viewer.imshow(img1, cmap=plt.get_cmap('gray')) # Loads the new image
    #plt.pause(0.01) # Delay in seconds
    fig.canvas.draw()
    #time.sleep(0.2)
