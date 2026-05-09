import json

with open('CogVSM.html', 'r', encoding='utf-8') as f:
    cogvsm = f.read()

with open('football-details.html', 'r', encoding='utf-8') as f:
    football = f.read()

with open('translations.js', 'r', encoding='utf-8') as f:
    js = f.read()

json_str = js.replace('window.TRANSLATIONS = ', '').rstrip(';\n')
tr = json.loads(json_str)

# ================================================================
# CogVSM.html
# ================================================================
c = cogvsm

c = c.replace('<link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">', '<link href="assets/img/favicon.png" rel="apple-touch-icon">')

c = c.replace(
    '  <header id="header" class="d-flex flex-column justify-content-center">\n\n  </header>',
    '  <header id="header" class="d-flex flex-column justify-content-center">\n    <a id="lang-btn" href="#" onclick="toggleLang(); return false;" class="flag-button">\n      <img id="lang-flag" src="https://flagicons.lipis.dev/flags/4x3/kr.svg" alt="Flag" class="flag-icon">\n      <span id="lang-text" class="flag-text">한국어</span>\n    </a>\n  </header>'
)

c = c.replace('<h2 style="color:#085a98;">Deep Reinforcement', '<h2 style="color:#085a98;" data-i18n="cogvsm.page_title">Deep Reinforcement')
c = c.replace('color: #f8893f; margin-bottom: 18px; text-align: center;">Enhancing', 'color: #f8893f; margin-bottom: 18px; text-align: center;" data-i18n="cogvsm.subtitle">Enhancing')
c = c.replace('margin-left: 5%; margin-right: 5%;">Video surveillance', 'margin-left: 5%; margin-right: 5%;" data-i18n="cogvsm.intro">Video surveillance')
c = c.replace('<h3 style="color: rgb(0, 87, 105);"><strong>Introduction:</strong>', '<h3 style="color: rgb(0, 87, 105);" data-i18n="cogvsm.intro_heading"><strong>Introduction:</strong>')
c = c.replace('width: 40%; margin-left: 5%;">\n                Efficient video', 'width: 40%; margin-left: 5%;" data-i18n="cogvsm.intro_body">\n                Efficient video')
c = c.replace('<h3 style="color: rgb(0, 87, 105);">Proposed Framework</h3>', '<h3 style="color: rgb(0, 87, 105);" data-i18n="cogvsm.framework_heading">Proposed Framework</h3>')
c = c.replace('margin-left: 10%; margin-right: 50%; margin-top: 0%; width: 80%; margin-top: 20px;" >', 'margin-left: 10%; margin-right: 50%; margin-top: 0%; width: 80%; margin-top: 20px;" data-i18n="cogvsm.framework_body">')
c = c.replace('<h3 style="color: rgb(0, 87, 105);">Results</h3>', '<h3 style="color: rgb(0, 87, 105);" data-i18n="cogvsm.results_heading">Results</h3>')
c = c.replace('width: 40%; margin-left: 5%; margin-top: 5%;">\n                  The sample simulated', 'width: 40%; margin-left: 5%; margin-top: 5%;" data-i18n="cogvsm.results_body">\n                  The sample simulated')
c = c.replace('<h2>Key Features</h2>', '<h2 data-i18n="cogvsm.features_heading">Key Features</h2>')
c = c.replace('<h4><a href="">Two-tiered Edge Computing</a></h4>', '<h4><a href="" data-i18n="cogvsm.feat1">Two-tiered Edge Computing</a></h4>')
c = c.replace('<h4><a href="">Dynamic Threshold Module</a></h4>', '<h4><a href="" data-i18n="cogvsm.feat2">Dynamic Threshold Module</a></h4>')
c = c.replace('<h4><a href="">Federated Learning (FL)</a></h4>', '<h4><a href="" data-i18n="cogvsm.feat3">Federated Learning (FL)</a></h4>')
c = c.replace('<h4><a href="">Deep Q-Network (DQN)</a></h4>', '<h4><a href="" data-i18n="cogvsm.feat4">Deep Q-Network (DQN)</a></h4>')
c = c.replace('<h3 style="color: rgb(0, 87, 105);">Two-Tiered Edge Computing</h3>', '<h3 style="color: rgb(0, 87, 105);" data-i18n="cogvsm.edge_heading">Two-Tiered Edge Computing</h3>')
c = c.replace('margin-left: 0%;width: 80%; margin-right: 2%; margin-top: 0%; width: 60%;" >\n                  In this project, the two-tiered', 'margin-left: 0%;width: 80%; margin-right: 2%; margin-top: 0%; width: 60%;" data-i18n="cogvsm.edge_body">\n                  In this project, the two-tiered')
c = c.replace('<h3 style="color: rgb(0, 87, 105);">DQN-based Controlling Threshold Module</h3>', '<h3 style="color: rgb(0, 87, 105);" data-i18n="cogvsm.dqn_heading">DQN-based Controlling Threshold Module</h3>')
c = c.replace('margin-left: 0%;width: 80%; margin-right: 2%; margin-top: 0%; width: 60%;" >\n                  The DQN-based dynamic', 'margin-left: 0%;width: 80%; margin-right: 2%; margin-top: 0%; width: 60%;" data-i18n="cogvsm.dqn_body">\n                  The DQN-based dynamic')
c = c.replace('<h3 style="color: rgb(0, 87, 105);">FL-based LSTM Module for Object Occurrence Prediction</h3>', '<h3 style="color: rgb(0, 87, 105);" data-i18n="cogvsm.fl_heading">FL-based LSTM Module for Object Occurrence Prediction</h3>')
c = c.replace('margin-left: 50%; margin-top: -250px; width: 45%; height: 45%;" >\n                  FL in this project', 'margin-left: 50%; margin-top: -250px; width: 45%; height: 45%;" data-i18n="cogvsm.fl_body">\n                  FL in this project')
c = c.replace(
    '<h4>Evaluation Results</h4>\n                  <div class="row">\n                    <p style="text-align: justify; font-size: 14px; width: 40%; margin-left: 7%; margin-top: 50px;">\n                      The evaluation of the FL-based',
    '<h4 data-i18n="cogvsm.eval_heading">Evaluation Results</h4>\n                  <div class="row">\n                    <p style="text-align: justify; font-size: 14px; width: 40%; margin-left: 7%; margin-top: 50px;" data-i18n="cogvsm.fl_eval_body">\n                      The evaluation of the FL-based',
    1
)
c = c.replace('<h3 style="color: rgb(0, 87, 105);">Deep RL-based Dynamic Controlling Threshold Module</h3>', '<h3 style="color: rgb(0, 87, 105);" data-i18n="cogvsm.drl_heading">Deep RL-based Dynamic Controlling Threshold Module</h3>')
c = c.replace('margin-left: 50%; margin-top: -250px; width: 45%; height: 45%;" >\n                  The DQN (Deep Q-Network)', 'margin-left: 50%; margin-top: -250px; width: 45%; height: 45%;" data-i18n="cogvsm.drl_body">\n                  The DQN (Deep Q-Network)')
c = c.replace(
    '<h4>Evaluation Results</h4>\n                  <div class="row">\n                    <p style="text-align: justify; font-size: 14px; width: 40%; margin-left: 7%; margin-top: 50px;">\n                      The evaluation of the DQN-based',
    '<h4 data-i18n="cogvsm.eval_heading">Evaluation Results</h4>\n                  <div class="row">\n                    <p style="text-align: justify; font-size: 14px; width: 40%; margin-left: 7%; margin-top: 50px;" data-i18n="cogvsm.drl_eval_body">\n                      The evaluation of the DQN-based',
    1
)
c = c.replace('<h3 style="color: rgb(0, 87, 105);">Performance Comparison</h3>', '<h3 style="color: rgb(0, 87, 105);" data-i18n="cogvsm.perf_heading">Performance Comparison</h3>')
c = c.replace('margin-left: 50%; margin-top: -300px; width: 45%; height: 45%;" >\n                  The evaluation results', 'margin-left: 50%; margin-top: -300px; width: 45%; height: 45%;" data-i18n="cogvsm.perf_body">\n                  The evaluation results')
c = c.replace(
    '<h4>Results</h4>\n                  <div class="row">\n                    <p style="text-align: justify; font-size: 14px; width: 40%; margin-left: 7%; margin-top: 100px;">\n                      The bar graph',
    '<h4 data-i18n="cogvsm.results_label">Results</h4>\n                  <div class="row">\n                    <p style="text-align: justify; font-size: 14px; width: 40%; margin-left: 7%; margin-top: 100px;" data-i18n="cogvsm.perf_results_body">\n                      The bar graph'
)
c = c.replace('<h4>Deep Reinforcement Learning-Empowered Cost-Effective Federated Video Surveillance Management Framework</h4>', '<h4 data-i18n="cogvsm.footer_title">Deep Reinforcement Learning-Empowered Cost-Effective Federated Video Surveillance Management Framework</h4>')
c = c.replace('<p>For more information</p>', '<p data-i18n="cogvsm.footer_info">For more information</p>')
c = c.replace('<i class="bx bx-book-reader"></i>&nbsp;&nbsp;Read Paper</a>', '<i class="bx bx-book-reader"></i>&nbsp;&nbsp;<span data-i18n="cogvsm.read_paper">Read Paper</span></a>')
c = c.replace('&copy; Copyright <strong><span>Dilshod B</span></strong>. All Rights Reserved\n      </div>', '<span data-i18n="common.copyright">&copy; Copyright <strong><span>Dilshod B</span></strong>. All Rights Reserved</span>\n      </div>')

with open('CogVSM.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('CogVSM.html done, data-i18n count:', c.count('data-i18n'))

# ================================================================
# football-details.html
# ================================================================
f2 = football

f2 = f2.replace('<link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">', '<link href="assets/img/favicon.png" rel="apple-touch-icon">')

f2 = f2.replace(
    '  <header id="header" class="d-flex flex-column justify-content-center">\n\n  </header>',
    '  <header id="header" class="d-flex flex-column justify-content-center">\n    <a id="lang-btn" href="#" onclick="toggleLang(); return false;" class="flag-button">\n      <img id="lang-flag" src="https://flagicons.lipis.dev/flags/4x3/kr.svg" alt="Flag" class="flag-icon">\n      <span id="lang-text" class="flag-text">한국어</span>\n    </a>\n  </header>'
)

f2 = f2.replace('<h2 ><a style="color:#085a98;">Football Analysis', '<h2><a style="color:#085a98;" data-i18n="football.page_title">Football Analysis')
f2 = f2.replace('font-size: 24px; color: #44965f; margin-bottom: 20px; text-align: center;">Are you', 'font-size: 24px; color: #44965f; margin-bottom: 20px; text-align: center;" data-i18n="football.subtitle">Are you')
f2 = f2.replace('<p style="text-align: left; font-size: 14px;">Enhanced Football', '<p style="text-align: left; font-size: 14px;" data-i18n="football.intro">Enhanced Football')
f2 = f2.replace('<h4 ><a style="color: rgb(0, 87, 105);">Highlights</a></h4>', '<h4><a style="color: rgb(0, 87, 105);" data-i18n="football.highlights_heading">Highlights</a></h4>')
f2 = f2.replace('<p style="text-align: left; font-size: 14px;" ><i class=\'bx bxs-badge-check\' style="color: crimson;"></i>&nbsp;', '<p style="text-align: left; font-size: 14px;" data-i18n="football.highlight1"><i class=\'bx bxs-badge-check\' style="color: crimson;"></i>&nbsp;')
f2 = f2.replace('<p style="text-align: left; font-size: 14px;" ><i class="bx bxs-badge-check" style="color:darkgoldenrod"></i>&nbsp;', '<p style="text-align: left; font-size: 14px;" data-i18n="football.highlight2"><i class="bx bxs-badge-check" style="color:darkgoldenrod"></i>&nbsp;')
f2 = f2.replace('<p style="text-align: left; font-size: 14px;"><i class="bx bxs-badge-check" style="color:green"></i>&nbsp;', '<p style="text-align: left; font-size: 14px;" data-i18n="football.highlight3"><i class="bx bxs-badge-check" style="color:green"></i>&nbsp;')
f2 = f2.replace('<p style="text-align: left; font-size: 14px;"><i class="bx bxs-badge-check" style="color:rgb(19, 0, 128)"></i>&nbsp;', '<p style="text-align: left; font-size: 14px;" data-i18n="football.highlight4"><i class="bx bxs-badge-check" style="color:rgb(19, 0, 128)"></i>&nbsp;')
f2 = f2.replace('<h2>Key Features</h2>', '<h2 data-i18n="football.features_heading">Key Features</h2>')
f2 = f2.replace('<h4><a>Deep Learning for Accurate Object Detection</a></h4>', '<h4><a data-i18n="football.feat1">Deep Learning for Accurate Object Detection</a></h4>')
f2 = f2.replace('<p style="text-align:justify; font-size: 14px;">This project encompasses', '<p style="text-align:justify; font-size: 14px;" data-i18n="football.feat1_body">This project encompasses')
f2 = f2.replace('<h4><a>Optical Flow-Empowered Consistent Object Tracking</a></h4>', '<h4><a data-i18n="football.feat2">Optical Flow-Empowered Consistent Object Tracking</a></h4>')
f2 = f2.replace('<p style="text-align: justify; font-size: 14px;">Optical flow refers', '<p style="text-align: justify; font-size: 14px;" data-i18n="football.feat2_body">Optical flow refers')
f2 = f2.replace('<h4><a>Categirized Team Players Using K-Means</a></h4>', '<h4><a data-i18n="football.feat3">Categorized Team Players Using K-Means</a></h4>')
f2 = f2.replace('<p style="text-align: left; font-size: 14px;">Team categorization involves', '<p style="text-align: left; font-size: 14px;" data-i18n="football.feat3_body">Team categorization involves')
f2 = f2.replace('<h3>Football Analysis</h3>', '<h3 data-i18n="football.footer_title">Football Analysis</h3>')
f2 = f2.replace('<p>For more information and documentation reference, click github icon below:</p>', '<p data-i18n="football.footer_info">For more information and documentation reference, click github icon below:</p>')
f2 = f2.replace('&copy; Copyright <strong><span>Dilshod B</span></strong>. All Rights Reserved\n      </div>', '<span data-i18n="common.copyright">&copy; Copyright <strong><span>Dilshod B</span></strong>. All Rights Reserved</span>\n      </div>')

with open('football-details.html', 'w', encoding='utf-8') as f:
    f.write(f2)
print('football-details.html done, data-i18n count:', f2.count('data-i18n'))

# ================================================================
# translations.js - add cogvsm.* and football.* keys
# ================================================================
tr['en'].update({
    'cogvsm.page_title': 'Deep Reinforcement Learning-Empowered Cost-Effective Federated Video Surveillance Management Framework',
    'cogvsm.subtitle': 'Enhancing Video Surveillance Efficiency with Deep Learning and Edge Computing',
    'cogvsm.intro': 'Video surveillance systems have become essential for safety and security, and the integration of deep learning (DL) has significantly improved their precision. However, DL-based surveillance requires substantial computational and memory resources, particularly for tasks like <strong>object tracking</strong> and <strong>object detection</strong>. Traditional video surveillance systems keep using GPU resources regardless of object absence in the video frames. Some recent approaches, for example, The <a href="https://www.mdpi.com/1424-8220/21/12/4089"><strong>AdaMM framework</strong></a> uses a constant threshold for releasing DL models in hierarchical edge computing, but this approach can lead to increased GPU memory consumption or frequent switching delays depending on the constant threshold value. The <a href="https://www.mdpi.com/1424-8220/23/5/2869"><strong>CogVSM framework</strong></a> uses LSTM predictions and EWMA smoothing to manage DL model releases, but it faces privacy issues and limitations due to the static smoothing factor\'s inability to adapt to varying scenarios. To address these demands, this study introduces an innovative video surveillance management system using a two-tiered edge computing architecture. The primary edge performs real-time object detection, reducing data transfer latency, while the secondary edge dynamically manages GPU usage with a novel threshold control module using Deep Q-Network (DQN) methods. Additionally, federated learning (FL) is utilized to train an LSTM network, ensuring data privacy and efficient resource allocation.',
    'cogvsm.intro_heading': '<strong>Introduction:</strong> Why Saving GPU Resources is So Crucial?',
    'cogvsm.intro_body': 'Efficient video surveillance, especially for abnormal behavior detection, heavily relies on Deep Learning (DL) models. These models require substantial GPU resources for tasks like <strong>object tracking</strong> and <strong>motion tracking</strong> in real-time. However, all traditional systems keep using allocated GPU resources even when there is no object in the video feed. So, saving GPU resources is crucial — we can utilize saved resources for other deep learning tasks, optimizing computational efficiency. By conserving GPU memory and computing power, surveillance systems can maintain responsiveness and handle more additional surveillance tasks. Thus, prioritizing GPU efficiency in video surveillance enhances overall system performance, bolstering safety and security in various environments.',
    'cogvsm.framework_heading': 'Proposed Framework',
    'cogvsm.framework_body': 'The proposed video surveillance management system for hierarchical edge computing comprises two connected edge nodes. The first node handles object detection using the YOLO algorithm, while the second node manages future object occurrence predictions with an FL-based LSTM, a DQN-based controlling threshold, and motion-tracking modules. The system starts by receiving video frames from an IP camera at the first node, where detected objects and relevant information are sent to the second node for further processing. In the second node, the FL-based LSTM module predicts future object occurrences and informs the DQN-based threshold control module, which makes binary decisions on adjusting threshold time values. The DQN model continually updates the threshold time based on its actions to optimize system performance. The primary contributions are the FL-based LSTM prediction and DQN-based controlling threshold modules, which enhance prediction accuracy and system efficiency.',
    'cogvsm.results_heading': 'Results',
    'cogvsm.results_body': 'The sample simulated video on the right demonstrates the <strong>real-time functionality</strong> of our project. The video features two terminals:<br>The first terminal, located on the bottom left, is dedicated to the <strong>server-side operations</strong>. It can handle up to <strong>10 clients simultaneously</strong>, analyzing human behavior through <strong>pose estimation models</strong>. The second terminal, positioned on the bottom right, is used for <strong>client-side operations</strong>, sending detected object frames and related detection information.<br>Additionally, the video displays <strong>pose estimation results</strong> and a <strong>line graph</strong> that plots <strong>real-time GPU memory usage</strong>.<br><strong>The main idea</strong> of the video is to show how <strong>dynamic model release</strong> works in real-time!!!',
    'cogvsm.features_heading': 'Key Features',
    'cogvsm.feat1': 'Two-tiered Edge Computing',
    'cogvsm.feat2': 'Dynamic Threshold Module',
    'cogvsm.feat3': 'Federated Learning (FL)',
    'cogvsm.feat4': 'Deep Q-Network (DQN)',
    'cogvsm.edge_heading': 'Two-Tiered Edge Computing',
    'cogvsm.edge_body': 'In this project, the two-tiered edge computing framework involves two interconnected edge nodes to optimize video surveillance tasks. The first tier focuses on real-time object detection using the YOLO algorithm, processing video frames directly from IP cameras. This immediate detection reduces latency by performing computational tasks close to the data source. The detected objects and relevant information are then sent to the second tier for advanced processing, which includes predicting future object occurrences using an FL-based LSTM model and making intelligent threshold decisions with a DQN model.<br>The advantages of this two-tiered approach include enhanced scalability and efficient resource utilization. By distributing tasks between the two nodes, the system alleviates computational load on any single node, leading to faster processing times and reduced network congestion.<br>Additionally, the use of FL at the second tier enhances data privacy and security by ensuring that sensitive data remains localized while still contributing to the training of robust predictive models. The adaptive threshold management by the DQN model further optimizes system performance by dynamically adjusting to changing conditions.',
    'cogvsm.dqn_heading': 'DQN-based Controlling Threshold Module',
    'cogvsm.dqn_body': 'The DQN-based dynamic controlling threshold module acts as the decision-making center that intelligently determines the controlling threshold time value in the overall system. Here, the threshold time value represents a timeout for deciding whether to hold or release the DL model. The DQN model receives the predicted object occurrence outcomes generated by the LSTM model. These prediction values are then used as state observations for the DQN model to make a crucial decision (i.e., whether to release or hold the DL model into action). The threshold time value is continually updated based on the DQN model\'s decision. If the DQN\'s action suggests holding the model, the motion-tracking threshold is incrementally increased by one second. Conversely, if the action indicates releasing the model, the threshold is decreased by one second, facilitating quicker response times to detected events.',
    'cogvsm.fl_heading': 'FL-based LSTM Module for Object Occurrence Prediction',
    'cogvsm.fl_body': 'FL in this project allows the LSTM model to be trained on data from multiple cameras without transferring the raw video data to a centralized server, preserving privacy and reducing the risk of data breaches. Each client optimizes a local model based on its data and shares this model with an FL server, which aggregates these local models to update a global model. This global model is then redistributed to all clients for further refinement, ensuring collaborative learning. By distributing the training process, FL optimizes resource usage, allowing for scalability and efficient utilization of processing power and storage capacity.',
    'cogvsm.eval_heading': 'Evaluation Results',
    'cogvsm.fl_eval_body': 'The evaluation of the FL-based LSTM model in this project demonstrates notable advantages despite some performance differences compared to centralized training. The model was trained for 200 rounds, with results measured using the RMSE metric, revealing that centralized training achieved a lower RMSE value of 0.79. However, the FL-based approach offers significant benefits in terms of data privacy and security by keeping data localized and enabling secure collaboration among multiple clients. This distributed training method also promotes scalability and resource efficiency. Consequently, the FL-based LSTM training is strongly recommended for scenarios where data privacy and ownership are critical.',
    'cogvsm.drl_heading': 'Deep RL-based Dynamic Controlling Threshold Module',
    'cogvsm.drl_body': 'The DQN (Deep Q-Network) model is employed to optimize the threshold time for releasing the DL model in the video surveillance system. This model-free approach relies on the predictions from the LSTM model, which captures temporal dependencies of object occurrences, as input to the DQN. The DQN model learns an optimal policy for threshold time adjustment based on these inputs, ensuring efficient resource utilization. By evaluating various factors such as object appearance patterns, system performance, and resource usage, the DQN intelligently decides when to trigger the DL model release. This results in improved overall effectiveness and efficiency of the smart video surveillance system, balancing GPU resource conservation and latency.',
    'cogvsm.drl_eval_body': 'The evaluation of the DQN-based controlling threshold module highlights its advantages in enhancing the energy efficiency of the video surveillance system. During training, the DQN model used LSTM predictions as input states and quickly learned to balance GPU memory savings with model reloading latency, achieving stable performance after about 50 episodes. The average cumulative reward, which grew rapidly in the initial 20 episodes, indicates the model\'s effectiveness in optimizing the threshold. Compared to the EWMA-based controlling module, the DQN-based approach showed superior sensitivity and faster response in anticipating object absence.',
    'cogvsm.perf_heading': 'Performance Comparison',
    'cogvsm.perf_body': 'The evaluation results highlighted in the figure showcase the advantages of the proposed framework in terms of efficient GPU memory utilization. The figure compares the performance of five different frameworks, demonstrating that the proposed framework, aided by LSTM predictions and DQN-based threshold control, outperformed others in managing GPU resources. The efficient release of GPU memory was particularly noticeable during intervals of object absence, where the proposed framework adapted swiftly to changing conditions. Compared to the AdaMM and CogVSM frameworks, which had varying memory usage based on fixed time values, the proposed framework dynamically optimized memory use, resulting in lower consumption and improved efficiency.',
    'cogvsm.results_label': 'Results',
    'cogvsm.perf_results_body': 'The bar graph in Figure 9 highlights the evaluation results of average GPU memory usage when \\(\\theta_m = 10\\) seconds. Our proposed framework demonstrated significantly optimized memory utilization at 29.23%, followed closely by our proposed framework with CNN at 30.11%. This efficiency stems from the novel integration of FL-based LSTM and DQN-based intelligent controlling threshold modules, which dynamically manage GPU resources based on real-time predictions and decisions. CogVSM also performed well at 31.43%, utilizing an LSTM model and statistical EWMA technique. AdaMM showed higher memory usage at 34.98%, while the baseline approach had the highest usage at 46.09%.',
    'cogvsm.footer_title': 'Deep Reinforcement Learning-Empowered Cost-Effective Federated Video Surveillance Management Framework',
    'cogvsm.footer_info': 'For more information',
    'cogvsm.read_paper': 'Read Paper',
    'cogvsm.github_btn': 'GitHub',
    'common.copyright': '&copy; Copyright <strong><span>Dilshod B</span></strong>. All Rights Reserved',
    'football.page_title': 'Football Analysis using Deep Learning and Computer Vision Techniques',
    'football.subtitle': 'Are you missing out on crucial insights from football matches?',
    'football.intro': 'Enhanced Football Analysis Project, the ultimate tool for in-depth match insights. Harnessing state-of-the-art AI and computer vision techniques, this project empowers teams and analysts to make data-driven decisions and optimize strategies. With the Football Analysis Project, you have access to advanced capabilities including YOLO for precise player and ball detection, Kmeans clustering for accurate team identification, optical flow for seamless player tracking despite dynamic camera movements, and perspective transformation for converting pixel data into real-world measurements.',
    'football.highlights_heading': 'Highlights',
    'football.highlight1': '<i class=\'bx bxs-badge-check\' style="color: crimson;"></i>&nbsp; <strong>Advanced AI Techniques:</strong> Leveraged YOLO for accurate object detection and tracking, ensuring precise identification of players, referees, and footballs within match footage.',
    'football.highlight2': '<i class="bx bxs-badge-check" style="color:darkgoldenrod"></i>&nbsp; <strong>Team Categorization:</strong> Utilized Kmeans clustering to categorize players into their respective teams based on shirt colors, enabling calculation of ball possession percentage and insights into team performance and strategy.',
    'football.highlight3': '<i class="bx bxs-badge-check" style="color:green"></i>&nbsp; <strong>Optical Flow for Consistent Tracking:</strong> Employed optical flow to assess camera movement between frames, maintaining tracking consistency despite dynamic camera motions for accurate player movement analysis.',
    'football.highlight4': '<i class="bx bxs-badge-check" style="color:rgb(19, 0, 128)"></i>&nbsp; <strong>Comprehensive Player Analysis:</strong> Calculated player speed and distance covered during matches, providing detailed performance metrics and insights into player performance and dynamics.',
    'football.features_heading': 'Key Features',
    'football.feat1': 'Deep Learning for Accurate Object Detection',
    'football.feat1_body': 'This project encompasses the utilization of cutting-edge artificial intelligence (AI) methodologies to enhance football match analysis. Leveraging advanced AI techniques involves employing sophisticated algorithms and models like YOLO (You Only Look Once) for object detection and tracking. YOLO is renowned for its ability to swiftly and accurately identify various objects within images or video frames, making it particularly suitable for real-time applications such as sports analytics. In the context of football analysis, YOLO is instrumental in precisely identifying players, referees, and footballs amidst the dynamic and fast-paced nature of the game.',
    'football.feat2': 'Optical Flow-Empowered Consistent Object Tracking',
    'football.feat2_body': 'Optical flow refers to the pattern of apparent motion of objects between consecutive frames in a sequence of images or video frames. In football analysis, optical flow techniques are employed to track player movements across frames, compensating for camera motion and ensuring consistent tracking accuracy. By analyzing the displacement of pixel intensities between frames, optical flow algorithms can estimate the velocity and direction of player movement, even in the presence of occlusions or scene changes. Consistent tracking enables analysts to accurately quantify player trajectories, measure positional changes, and identify key events such as goal-scoring opportunities, tackles, or passes.',
    'football.feat3': 'Categorized Team Players Using K-Means',
    'football.feat3_body': 'Team categorization involves the process of classifying players into their respective teams based on visual cues, particularly the colors of their jerseys. This highlight emphasizes the use of Kmeans clustering, a machine learning algorithm, to perform pixel segmentation and group pixels of similar colors together. In the context of football analysis, Kmeans clustering enables the automatic identification and categorization of players into distinct teams, thereby facilitating subsequent analysis such as ball possession percentage calculations and team performance evaluation.',
    'football.footer_title': 'Football Analysis',
    'football.footer_info': 'For more information and documentation reference, click github icon below:',
})

tr['ko'].update({
    'cogvsm.page_title': '심층 강화 학습을 통한 비용 효율적인 연합 비디오 감시 관리 프레임워크',
    'cogvsm.subtitle': '딥러닝과 엣지 컴퓨팅으로 비디오 보안 감시 효율성 향상',
    'cogvsm.intro': '비디오 감시 시스템은 안전과 보안을 위해 필수적이며, 딥러닝(DL)의 통합으로 그 정밀도가 크게 향상되었습니다. 그러나 DL 기반 감시는 <strong>객체 추적</strong> 및 <strong>객체 탐지</strong>와 같은 작업에 많은 계산 및 메모리 자원이 필요합니다. 전통적인 비디오 감시 시스템은 프레임에 객체가 없더라도 GPU 자원을 지속적으로 사용합니다. 좌단한 <a href="https://www.mdpi.com/1424-8220/21/12/4089"><strong>AdaMM 프레임워크</strong></a>는 계층적 엣지 컴퓨팅에서 DL 모델 해제를 위해 일정한 임계값을 사용하지만 경우에 따라 GPU 메모리 소비 증가 또는 빈번한 전환 지연을 초래할 수 있습니다. <a href="https://www.mdpi.com/1424-8220/23/5/2869"><strong>CogVSM 프레임워크</strong></a>는 LSTM 예측 및 EWMA 스무딩을 사용하여 DL 모델 해제를 관리하지만 프라이버시 문제와 EWMA의 정적 스무딩 계수의 한계가 있습니다. 본 연구는 이중 계층 엣지 컴퓨팅 아키텍처를 사용하는 혁신적인 비디오 감시 관리 시스템을 소개합니다. 1차 엣지는 실시간 객체 탐지를 수행하고, 2차 엣지는 DQN 방법을 통해 GPU 메모리와 모델 재로드 지연의 균형을 최적화합니다. 연합 학습(FL)을 통해 LSTM 네트워크를 훈련하여 데이터 프라이버시와 효율적인 자원 할당을 보장합니다.',
    'cogvsm.intro_heading': '<strong>소개:</strong> 왜 GPU 자원 절약이 중요한가?',
    'cogvsm.intro_body': '효율적인 비디오 감시는 특히 이상 행동 탐지를 위해 딥러닝(DL) 모델에 크게 의존합니다. 이러한 모델은 실시간 <strong>객체 추적</strong> 및 <strong>동작 추적</strong>과 같은 작업에 상당한 GPU 자원이 필요합니다. 그러나 전통적인 시스템은 비디오 피드에 객체가 없더라도 할당된 GPU 자원을 계속 사용합니다. GPU 자원을 절약하는 것은 절약된 자원을 다른 딥러닝 작업에 활용할 수 있어 계산 효율성을 최적화할 수 있기 때문에 매우 중요합니다. GPU 메모리와 계산 능력을 절약함으로써 감시 시스템은 반응성을 유지하고 추가적인 감시 작업을 더 많이 처리할 수 있습니다.',
    'cogvsm.framework_heading': '제안된 프레임워크',
    'cogvsm.framework_body': '계층적 엣지 컴퓨팅을 위한 제안된 비디오 감시 관리 시스템은 두 개의 연결된 엣지 노드로 구성됩니다. 첫 번째 노드는 YOLO 알고리즘을 사용하여 객체 감지를 수행하며, 두 번째 노드는 FL 기반의 LSTM, DQN 기반의 제어 임계값, 동작 추적 모듈을 사용하여 미래 객체 발생 예측을 관리합니다. 시스템은 IP 카메라로부터 비디오 프레임을 첫 번째 노드에서 수신하여 감지된 객체와 관련 정보를 두 번째 노드로 전송합니다. 두 번째 노드에서 FL 기반의 LSTM 모듈은 미래 객체 발생을 예측하고 DQN 기반의 임계값 제어 모듈에 정보를 제공하여 임계값 시간 값을 조정하는 이진 결정을 내립니다.',
    'cogvsm.results_heading': '결과',
    'cogvsm.results_body': '오른쪽의 샘플 시뮬레이션 비디오는 프로젝트의 <strong>실시간 기능</strong>을 보여줍니다. 비디오는 두 개의 터미널을 포함합니다:<br>왼쪽 하단에 위치한 첫 번째 터미널은 <strong>서버 측 작업</strong>을 전담합니다. 이 터미널은 <strong>최대 10명의 클라이언트를 동시에</strong> 처리할 수 있으며, <strong>포즈 추정 모델</strong>을 통해 인간 행동을 분석합니다. 오른쪽 하단에 위치한 두 번째 터미널은 <strong>클라이언트 측 작업</strong>에 사용됩니다.<br>또한, 비디오는 <strong>포즈 추정 결과</strong>와 <strong>실시간 GPU 메모리 사용량</strong>을 나타내는 <strong>선 그래프</strong>를 보여줍니다.<br><strong>동적 모델 릴리즈</strong>가 실시간으로 어떻게 작동하는지 보여주는 것이 주요 아이디어입니다!!!',
    'cogvsm.features_heading': '주요 기능',
    'cogvsm.feat1': '이중 계층 엣지 컴퓨팅',
    'cogvsm.feat2': '동적 임계값 모듈',
    'cogvsm.feat3': '연합 학습 (FL)',
    'cogvsm.feat4': '딥 Q-네트워크 (DQN)',
    'cogvsm.edge_heading': '이중 계층 엣지 컴퓨팅',
    'cogvsm.edge_body': '이 프로젝트에서 이중 계층 엣지 컴퓨팅 프레임워크는 비디오 감시 작업을 최적화하기 위해 두 개의 상호 연결된 엣지 노드를 포함합니다. 첫 번째 계층은 YOLO 알고리즘을 사용하여 IP 카메라에서 직접 비디오 프레임을 처리하여 실시간 객체 감지에 중점을 둑니다. 감지된 객체와 관련 정보는 이후 두 번째 계층으로 전송되어 FL 기반 LSTM 모델을 사용한 미래 객체 발생 예측과 DQN 모델을 이용한 지능형 임계값 결정 등의 고급 처리가 이루어집니다. 이중 계층 접근 방식의 장점에는 향상된 확장성과 효율적인 자원 활용이 포함됩니다. 두 노드 간에 작업을 분산시킴으로써 시스템은 단일 노드의 계산 부하를 줄이고 더 빠른 처리 시간과 감소된 네트워크 혼잡을 달성합니다.',
    'cogvsm.dqn_heading': 'DQN 기반 임계값 제어 모듈',
    'cogvsm.dqn_body': 'DQN 기반 동적 임계값 제어 모듈은 시스템 전체에서 임계값 시간을 지능적으로 결정하는 의사 결정 센터 역할을 합니다. 임계값 시간은 DL 모델을 유지하거나 해제할지를 결정하기 위한 타임아웃을 나타냅니다. DQN 모델은 LSTM 모델이 생성한 예측된 객체 발생 결과를 수신하여 이를 상태 관측치로 활용하여 DL 모델을 릴리즈할지 유지할지 결정합니다. DQN의 행동이 모델 유지를 제안하면 모션 추적 임계값이 1초 증가하고, 모델 해제를 나타내면 임계값이 1초 감소하여 더 빠른 응답 시간을 용이하게 합니다.',
    'cogvsm.fl_heading': 'FL 기반 LSTM 모듈을 통한 객체 발생 예측',
    'cogvsm.fl_body': '이 프로젝트에서 FL은 LSTM 모델이 여러 카메라의 데이터를 기반으로 학습할 수 있도록 하며, 중앙 서버에 원시 비디오 데이터를 전송하지 않으멇 프라이버시를 보호하고 데이터 유출 위험을 줄입니다. 각 클라이언트는 자신의 데이터로 로컈 모델을 최적화하고 FL 서버와 공유하며, FL 서버는 이를 집계하여 글로벌 모델을 업데이트합니다. 이 글로벌 모델은 모든 클라이언트에 다시 배포되어 추가적인 개선이 이루어집니다. 이 방식은 학습 과정을 분산시켜 자원 사용을 최적화하며 확장성과 효율적인 모델 학습을 가능하게 합니다.',
    'cogvsm.eval_heading': '평가 결과',
    'cogvsm.fl_eval_body': '이 프로젝트에서 FL 기반 LSTM 모델의 평가는 중앙 집중식 학습과 비교하여 성능 차이가 있지만 주목할 만한 장점을 보여줍니다. 모델은 200 라운드 동안 학습되었으며, RMSE 메트릭을 사용하여 결과를 측정한 결과 중앙 집중식 학습이 0.79의 낙은 RMSE 값을 달성했습니다. 그러나 FL 기반 접근 방식은 데이터가 로컈화되어 보관되며 여러 클라이언트 간의 안전한 협업이 가능하여 데이터 프라이버시와 보안 측면에서 중요한 이점을 제공합니다. 이 분산 학습 방법은 확장성과 자원 효율성도 촉진합니다.',
    'cogvsm.drl_heading': '딥 RL 기반 동적 임계값 제어 모듈',
    'cogvsm.drl_body': 'DQN (Deep Q-Network) 모델은 비디오 감시 시스템에서 DL 모델을 해제하기 위한 임계값 시간을 최적화하는 데 사용됩니다. 이 모델 비의존 접근 방식은 객체 발생의 시간적 의존성을 포왕하는 LSTM 모델의 예측 결과를 DQN의 입력으로 활용합니다. DQN 모델은 이러한 입력을 바탕으로 임계값 시간 조정에 대한 최적의 정책을 학습하여 자원 활용의 효율성을 보장합니다. 이로 인해 GPU 자원 절약과 지연 시간을 균형 있게 조절하여 스마트 비디오 감시 시스템의 전체적인 효과성과 효율성을 개선합니다.',
    'cogvsm.drl_eval_body': 'DQN 기반 임계값 제어 모듈의 평가는 비디오 감시 시스템의 에너지 효율성을 향상시키는 장점을 강조합니다. 훈련 동안 DQN 모델은 LSTM 예측을 입력 상태로 사용하여 GPU 메모리 절약과 모델 재로딩 지연 시간을 균형 있게 조절하며, 약 50 에피소드 훈 안정적인 성능을 달성했습니다. 초기 20 에피소드 동안 급격히 증가한 평균 누적 보상은 임계값 최적화에서 모델의 효과성을 나타냅니다. EWMA 기반 제어 모듈과 비교했을 때, DQN 기반 접근 방식은 객체 부재를 예상하는 민감도와 반응 속도에서 우수한 성과를 보였습니다.',
    'cogvsm.perf_heading': '성능 비교',
    'cogvsm.perf_body': '오른쪽 그림에 강조된 평가 결과는 GPU 메모리 활용 효율성 측면에서 제안된 프레임워크의 장점을 보여줍니다. 이 그림은 다섯 가지 기존 프레임워크의 성능을 비교하며, LSTM 예측과 DQN 기반 임계값 제어가 지원하는 제안된 프레임워크가 GPU 자원 관리에서 다른 프레임워크보다 우수한 성과를 보였음을 나타냅니다. 객체 부재 간격 동안 GPU 메모리의 효율적인 해제는 제안된 프레임워크가 변화하는 조건에 신속하게 적응했음을 보여줍니다.',
    'cogvsm.results_label': '결과',
    'cogvsm.perf_results_body': '그림 9의 막대 그래프는 \\(\\theta_m = 10\\) 초일 때의 평균 GPU 메모리 사용 평가 결과를 강조합니다. 제안된 프레임워크는 29.23%로 메모리 활용이 현저하게 최적화되었으며, CNN을 사용할 때 제안된 프레임워크는 30.11%로 뒤를 이었습니다. 이 효율성은 FL 기반 LSTM과 DQN 기반 지능형 제어 임계값 모듈의 혁신적 통합 덕분으로, 실시간 예측 및 결정에 따라 GPU 자원을 동적으로 관리합니다. CogVSM은 31.43%로 성과를 보였고, AdaMM은 34.98%, 기본 접근 방식은 46.09%로 가장 높은 사용량을 기록했습니다.',
    'cogvsm.footer_title': '심층 강화 학습을 통한 비용 효율적인 연합 비디오 감시 관리 프레임워크',
    'cogvsm.footer_info': '자세한 정보',
    'cogvsm.read_paper': '논문을 읽기',
    'cogvsm.github_btn': '깃허브',
    'common.copyright': '&copy; 저작권 <strong><span>Dilshod B</span></strong>. 판권 소유',
    'football.page_title': '딥러닝 및 컴퓨터 비전 기법을 활용한 축구 분석',
    'football.subtitle': '축구 경기에서 중요한 통찰을 놓치고 있습니까?',
    'football.intro': '고급 축구 분석 프로젝트는 심층 경기 통찰력을 위한 궁극의 도구입니다. 최첨단 AI 및 컴퓨터 비전 기법을 활용하여 이 프로젝트는 팀과 분석가가 데이터 기반 결정을 내리고 전략을 최적화할 수 있도록 지원합니다. YOLO를 사용한 정확한 선수 및 공 탐지, Kmeans 클러스터링을 통한 정확한 팀 식별, 동적 카메라 움직임에도 불구하고 일관된 선수 추적을 위한 옷티컴 플로우, 픽셀 데이터를 실제 측정치로 변환하기 위한 투시 변환 등 고급 기능을 제공합니다.',
    'football.highlights_heading': '주요 하이라이트',
    'football.highlight1': '<i class=\'bx bxs-badge-check\' style="color: crimson;"></i>&nbsp; <strong>고급 AI 기법:</strong> YOLO를 활용하여 정확한 객체 탐지 및 추적을 수행하여 경기 영상 내에서 선수, 심판, 축구공을 정확하게 식별합니다.',
    'football.highlight2': '<i class="bx bxs-badge-check" style="color:darkgoldenrod"></i>&nbsp; <strong>팀 분류:</strong> Kmeans 클러스터링을 활용하여 셔츠 색상에 따라 선수를 각 팀으로 분류하고, 볼 점유율 계산 및 팀 성과와 전략에 대한 통찰을 제공합니다.',
    'football.highlight3': '<i class="bx bxs-badge-check" style="color:green"></i>&nbsp; <strong>일관된 추적을 위한 옷티컴 플로우:</strong> 프레임 간 카메라 움직임을 평가하여 동적 카메라 움직임에도 불구하고 일관된 추적을 유지하여 정확한 선수 이동 분석을 수행합니다.',
    'football.highlight4': '<i class="bx bxs-badge-check" style="color:rgb(19, 0, 128)"></i>&nbsp; <strong>종합 선수 분석:</strong> 경기 중 선수의 속도와 이동 거리를 계산하여 선수 성과와 역학에 대한 세부적인 메트릭과 통찰을 제공합니다.',
    'football.features_heading': '주요 기능',
    'football.feat1': '정확한 객체 감지를 위한 딥 러닝',
    'football.feat1_body': '이 프로젝트는 최신 인공지능(AI) 기법을 활용하여 축구 경기 분석을 향상시키는 것을 목표로 합니다. 첨단 AI 기술을 활용하는 것은 YOLO(You Only Look Once)와 같은 정교한 알고리즘과 모델을 사용하여 객체 감지 및 추적을 포함합니다. YOLO는 이미지나 비디오 프레임 내에서 다양한 객체를 빠르고 정확하게 식별하는 능력으로 잘 알려져 있으며, 스포츠 분석과 같은 실시간 응용 프로그램에 특히 적합합니다. 축구 분석의 맥락에서 YOLO는 게임의 동적이고 빠른 속도 속에서 선수, 심판 및 축구공을 정확하게 식별하는 데 필수적입니다.',
    'football.feat2': '옷티컴 플로우 기반 일관된 객체 추적',
    'football.feat2_body': '광학 흐름은 이미지나 비디오 프레임의 연속적인 장면 간에 객체의 걉보기 움직임 패턴을 나타냅니다. 축구 분석에서 광학 흐름 기법은 프레임 간의 선수 이동을 추적하는 데 사용되며, 카메라의 움직임을 보정하고 일관된 추적 정확성을 보장합니다. 프레임 간 픽셀 강도의 변위를 분석함으로써 광학 흐름 알고리즘은 가림이나 장면 변화가 있는 상황에서도 선수의 이동 속도와 방향을 추정할 수 있습니다. 일관된 추적은 분석가가 선수의 군적를 정확하게 정량화하고, 위치 변화를 측정하며, 골 슬코어링 기회, 태클 또는 패스와 같은 주요 이벤트를 식별할 수 있도록 지원합니다.',
    'football.feat3': 'K-평균을 이용한 팀 선수 분류',
    'football.feat3_body': '팀 분류는 선수들을 시각적 단서, 특히 유니폼 색상을 기준으로 각 팀에 맞게 분류하는 과정을 포함합니다. K-평균 군집화를 사용하여 픽셀 세그먼테이션을 수행하고 유사한 색상의 픽셀을 그룹화합니다. 축구 분석의 맥락에서 K-평균 군집화는 선수들을 자동으로 식별하고 명확하게 다른 팀으로 분류하여 볼 점유율 계산 및 팀 성과 평가와 같은 후속 분석을 용이하게 합니다. 선수를 정확하게 팀으로 분류함으로써 분석가는 팀의 역학, 포메이션 전략, 경기 중 선수 상호 작용에 대한 통찰을 얻을 수 있습니다.',
    'football.footer_title': '축구 분석',
    'football.footer_info': '자세한 정보와 문서 참조를 원하시면 아래의 GitHub 아이콘을 클릭하세요:',
})

# Write updated translations.js
new_js = 'window.TRANSLATIONS = ' + json.dumps(tr, ensure_ascii=False, indent=2) + ';\n'
with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(new_js)
print('translations.js updated')

# Delete Korean HTML files
import os
for fname in ['index - korean.html', 'CogVSM - korean.html', 'football-details - korean.html']:
    if os.path.exists(fname):
        os.remove(fname)
        print(f'Deleted: {fname}')

print('All done!')