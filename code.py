
import os
import shutil
import json

# Load the provided JSON data again
with open('e:/web development/testargon/Datavisualization/transformed_data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    
# Redefine the HTML template to add a note about log transformation and a brief data analysis

html_template = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>雷达图 - {country}</title>
  <meta content="" name="description">
  <meta content="" name="keywords">
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <!-- Favicons -->
  <link href="../assets/" rel="icon">
  <link href="../assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.gstatic.com" rel="preconnect">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="../assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="../assets/vendor/quill/quill.snow.css" rel="stylesheet">
  <link href="../assets/vendor/quill/quill.bubble.css" rel="stylesheet">
  <link href="../assets/vendor/remixicon/remixicon.css" rel="stylesheet">
  <link href="../assets/vendor/simple-datatables/style.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="../assets/css/style.css" rel="stylesheet">

  <!-- =======================================================
  * Template Name: NiceAdmin
  * Updated: Jul 27 2023 with Bootstrap v5.3.1
  * Template URL: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/
  * Author: BootstrapMade.com
  * License: https://bootstrapmade.com/license/
  ======================================================== -->
</head>

<body>


  <!-- ======= Header ======= -->
  <header id="header" class="header fixed-top d-flex align-items-center">

    <div class="d-flex align-items-center justify-content-between">
      <a href="../index.html" class="logo d-flex align-items-center">
        <img src="../assets/img/科学.png" alt="">
        <span class="d-none d-lg-block">科学分工</span>
      </a>
      <i class="bi bi-list toggle-sidebar-btn"></i>
    </div>

  </header><!-- End Header -->

  <!-- ======= Sidebar ======= -->
  <aside id="sidebar" class="sidebar">

    <ul class="sidebar-nav" id="sidebar-nav">

      <li class="nav-item">
        <a class="nav-link collapsed" href="../index.html">
          <i class="bi bi-person"></i>
          <span>主页</span>
        </a>
      </li><!-- End Home page Nav -->

      <li class="nav-item">
        <a class="nav-link collapsed" data-bs-target="#charts-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-bar-chart"></i><span>地图可视化</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="charts-nav" class="nav-content collapse" data-bs-parent="#sidebar-nav">
          <li>
            <a href="../资源.html">
              <i class="bi bi-circle"></i><span>资源</span>
            </a>
          </li>
          <li>
            <a href="../经济.html">
              <i class="bi bi-circle"></i><span>经济</span>
            </a>
          </li>
          <li>
            <a href="../地方问题.html">
              <i class="bi bi-circle"></i><span>地方问题</span>
            </a>
          </li>
          <li>
            <a href="../国家政策.html">
              <i class="bi bi-circle"></i><span>国家政策</span>
            </a>
          </li>
        </ul>
      </li><!-- End Charts Nav -->

      <li class="nav-item">
        <a class="nav-link" data-bs-target="#radar-nav" data-bs-toggle="collapse" href="#">
          <i class="bx bx-radar"></i><span>雷达图可视化</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="radar-nav" class="nav-content collapse show" data-bs-parent="#sidebar-nav">
          <li>
            <a href="../Example.html">
              <i class="bi bi-circle"></i><span>示例</span>
            </a>
          </li>
          <li>
            <a href="../search.html" class="active">
              <i class="bi bi-circle"></i><span>检索</span>
            </a>
          </li>
        </ul>
      </li><!-- End radar Nav -->
      </ul>
  </aside><!-- End Sidebar-->

  <main id="main" class="main">

    <div class="pagetitle">
      <h1>检索结果</h1>
      <nav>
        <ol class="breadcrumb">
          <li class="breadcrumb-item"><a href="../index.html">主页</a></li>
          <li class="breadcrumb-item">雷达图</li>
          <li class="breadcrumb-item active">检索</li>
        </ol>
      </nav>
    </div><!-- End Page Title -->

    <p>数据经对数变换处理。<span class="text-muted">Data displayed in the radar chart has been transformed using a logarithmic scale to reduce the differences in scale.</span> </p>

    <section class="section">
      <div class="row">

        <div>
          <div class="card" id="card1">
            <div class="card-body">
              <h5 class="card-title">{country}</h5>
              <div class="text-center">
              <div class="position-relative">
              <!-- Radar Chart -->
              <div id="radarPlot"></div>
              <input type="range" min="0" max="{max_index}" value="0" id="yearSlider" style="width: 100%;">
              <p id="yearLabel">Year: {start_year}</p>
              <script>
                    const countryData = {data};
                    const yearSlider = document.getElementById('yearSlider');
                    const yearLabel = document.getElementById('yearLabel');

                    function logTransform(value) {{
                        // Apply log transformation and handle values <= 0 by setting them to a small positive value
                        return Math.log(value > 0 ? value : 1e-9) + 1;
                    }}

                    function updatePlot(index) {{
                        const currentDataPoint = countryData[index].data;
                        Plotly.update("radarPlot", {{
                            r: [currentDataPoint.map(d => logTransform(d.value))],
                            theta: [currentDataPoint.map(d => d.axis)],
                            name: [countryData[index].year]
                        }});
                        yearLabel.textContent = "Year: " + countryData[index].year;
                    }}

                    yearSlider.addEventListener('input', function() {{
                        updatePlot(yearSlider.value);
                    }});

                    const maxScaleValue = Math.max(...countryData.map(entry => Math.max(...entry.data.map(d => logTransform(d.value)))));
                    const plotData = [{{
                        type: 'scatterpolar',
                        r: countryData[0].data.map(d => logTransform(d.value)),
                        theta: countryData[0].data.map(d => d.axis),
                        fill: 'toself',
                        name: countryData[0].year
                    }}];
                    const layout = {{
                        title: '{country}',
                        polar: {{
                            radialaxis: {{
                                visible: true,
                                range: [0, maxScaleValue] 
                            }}
                        }},
                        showlegend: true
                    }};
                    Plotly.newPlot("radarPlot", plotData, layout);
              </script>
              <!-- End Radar CHart -->
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>

      <div class="col-lg-12">
        <div class="card" id="card1">
          <div class="card-body">
            <h5 class="card-title">数据分析 Data Analysis</h5>
            <div class="text-left">
            <div class="position-relative">
              <p>该雷达图展现了该国学科发展随时间的变化情况。对于数据的对数处理能够弥合尺度上的差异，而较好地反应该国自身学科发展情况。时间轴滑块能够让用户自主选择需要考察的时间段，并展示整体变化趋势。该趋势的成因及影响可以结合诸多领域进行更深入的考察。</p>
              <p class="text-muted">This radar chart visualizes various metrics for China over different years. The logarithmic transformation provides a more balanced view of metrics, especially when there are significant variances in the original scale. By using the slider, it's possible to observe the evolution of these metrics over time. Note that specific insights would require a deeper understanding of the contextual background of the data.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    <section class="section">
      <div class="row">

        <div class="container mt-4">

          <div class="card">
              <div class="card-header">
                  <!-- 搜索栏 -->
                  <div class="input-group">
                      <input type="text" class="form-control" id="countryInput" placeholder="China...">
                      <button class="btn btn-outline-secondary" id="searchButton" type="button">Search</button>
                  </div>
              </div>
              <div class="card-body">
                  <!-- 卡片内容 -->
                  <h5 class="card-title" id="cardTitle">单独检索 Individual Search</h5>
                  <p>请输入您检索国家或地区的英文名。</p>
                  <p class="card-text text-muted">Please enter the English name of the country or region you are searching for.</p>
              </div>
          </div>

          <div class="card">
            <div class="card-header">
                <!-- 搜索栏 -->
                <div class="input-group">
                    <input type="text" class="form-control" id="countryInput2" placeholder="China...">
                    <input type="text" class="form-control" id="countryInput3" placeholder="Germany...">
                    <button class="btn btn-outline-secondary" id="searchButton2" type="button">Search</button>
                </div>
            </div>
            <div class="card-body">
                <!-- 卡片内容 -->
                <h5 class="card-title" id="cardTitle2">对比检索 Compare Search</h5>
                <p>请输入您检索国家或地区的英文名。注意：时间轴范围由左侧国家或地区决定。</p>
                <p class="card-text text-muted">Please enter the English name of the country or region you are searching for. Note: The time axis range is determined by the left country or region.</p>
            </div>
        </div>
        
      </div>
      
      <script>
          const searchButton = document.getElementById("searchButton");
          const countryInput = document.getElementById("countryInput");
          const cardTitle = document.getElementById("cardTitle");
      
          searchButton.addEventListener("click", function() {{
              const inputText = countryInput.value.trim() + ".html";
              
              // 根据输入文本进行页面跳转或修改标题颜色
              var countrylist = ['Afghanistan.html', 'Albania.html', 'Algeria.html', 'Andorra.html', 'Angola.html', 'Antarctica.html', 'Antigua & Barbuda.html', 'Argentina.html', 'Armenia.html', 'Australia.html', 'Austria.html', 'Azerbaijan.html', 'Bahamas.html', 'Bahrain.html', 'Bangladesh.html', 'Barbados.html', 'Belgium.html', 'Belize.html', 'Benin.html', 'Bermuda.html', 'Bhutan.html', 'Bolivia.html', 'Bophuthatswana.html', 'Bosnia & Herzegovina.html', 'Botswana.html', 'Brazil.html', 'Brunei.html', 'Bulgaria.html', 'Burkina Faso.html', 'Burma.html', 'Burundi.html', 'Byelarus.html', 'Cambodia.html', 'Cameroon.html', 'Canada.html', 'Cape Verde.html', 'Central African Republic.html', 'Ceylon.html', 'Chad.html', 'Chile.html', 'China.html', 'Ciskei.html', 'Colombia.html', 'Comoros.html', 'Congo.html', 'Cook Islands.html', 'Costa Rica.html', 'Crimea.html', 'Croatia.html', 'Cuba.html', 'Cyprus.html', 'Czech Republic.html', 'Czechoslovakia.html', 'Dahomey.html', 'Democratic Republic of the Congo.html', 'Denmark.html', 'Djibouti.html', 'Dominica .html', 'Dominican Republic.html', 'Ecuador.html', 'Egypt.html', 'El Salvador.html', 'Equatorial Guinea.html', 'Eritrea.html', 'Estonia.html', 'Ethiopia.html', 'Federated States of Micronesia .html', 'Fiji.html', 'Finland.html', 'France.html', 'French-Guiana.html', 'French-Polynesia.html', 'Gabon.html', 'Gambia.html', 'Georgia.html', 'Germany.html', 'Ghana .html', 'Gilbert & Ellice Islands.html', 'Greece.html', 'Grenada.html', 'Guadeloupe.html', 'Guatemala.html', 'Guinea-Bissau.html', 'Guinea.html', 'Guyana.html', 'Haiti.html', 'Honduras .html', 'Hong-Kong.html', 'Hungary.html', 'Iceland.html', 'India.html', 'Indonesia.html', 'Iran.html', 'Iraq.html', 'Ireland.html', 'Israel.html', 'Italy.html', 'Ivory Coast.html', 'Jamaica.html', 'Japan.html', 'Jordan.html', 'Kazakhstan.html', 'Kenya.html', 'Khmer Republic.html', 'Kiribati.html', 'Kuwait.html', 'Kyrgyzstan.html', 'Laos.html', 'Latvia.html', 'Lebanon .html', 'Lesotho.html', 'Liberia .html', 'Libya.html', 'Liechtenstein.html', 'Lithuania.html', 'Luxembourg.html', 'Macau.html', 'Macedonia.html', 'Madagascar.html', 'Malawi.html', 'Malaysia.html', 'Maldives.html', 'Mali.html', 'Malta.html', 'Marshall Islands.html', 'Mauritania.html', 'Mauritius.html', 'Mexico.html', 'Moldova .html', 'Monaco.html', 'Mongolia.html', 'Montenegro.html', 'Morocco.html', 'Mozambique.html', 'Namibia.html', 'Nauru.html', 'Nepal.html', 'Netherlands-Antilles.html', 'Netherlands.html', 'New Zealand.html', 'New-Caledonia.html', 'Nicaragua.html', 'Niger.html', 'Nigeria.html', 'Niue.html', 'North Korea.html', 'Norway.html', 'Oman.html', 'Pakistan.html', 'Palau.html', 'Palestine.html', 'Panama.html', 'Papua New Guinea.html', 'Paraguay.html', "People's Democratic Republic of Yemen.html", "People's Republic of Congo.html", 'Peru.html', 'Philippines.html', 'Poland.html', 'Portugal.html', 'Qatar.html', 'Republic of Kosovo.html', 'Republic of Serbia.html', 'Reunion.html', 'Rhodesia.html', 'Romania.html', 'Russia.html', 'Rwanda.html', 'Saint-Vincent-et-les-Grenadines.html', 'Samoa.html', 'San Marino.html', 'Sao Tome & Principe.html', 'Saudi Arabia.html', 'Senegal.html', 'Senegambia.html', 'Serbia and Montenegro.html', 'Seychelles.html', 'Sierra Leone.html', 'Singapore.html', 'Slovakia.html', 'Slovenia.html', 'Solomon Islands.html', 'Somalia.html', 'South Africa.html', 'South Korea.html', 'South Sudan.html', 'Spain.html', 'Sri Lanka.html', 'St-Kitts & Nevis .html', 'St-Lucia.html', 'Sudan.html', 'Suriname.html', 'Swaziland.html', 'Sweden.html', 'Switzerland.html', 'Syria.html', 'Taiwan.html', 'Tajikistan.html', 'Tanzania.html', 'Thailand.html', 'Togo.html', 'Tonga.html', 'Transkei.html', 'Trinidad and Tobago.html', 'Tunisia.html', 'Turkey.html', 'Turkmenistan.html', 'Tuvalu.html', 'Uganda.html', 'Ukraine.html', 'Union of Soviet Socialist Republics.html', 'United Arab Emirates.html', 'United Arab Republic.html', 'United Kingdom.html', 'United States.html', 'Uruguay.html', 'Uzbekistan.html', 'Vanuatu.html', 'Vatican.html', 'Venda.html', 'Venezuela.html', 'Vietnam.html', 'Western Sahara.html', 'Yemen Arab Republic.html', 'Yemen.html', 'Yugoslavia.html', 'Zaire.html', 'Zambia.html', 'Zimbabwe.html']
              
              if (countrylist.includes(inputText)) {{
                  window.location.href = inputText ; // 根据文件名进行页面跳转
              }} else {{
                  cardTitle.style.color = "purple";
                  cardTitle.textContent = "抱歉，您输入的国家或地区名有误。";
              }}

          }});
          const searchButton2 = document.getElementById("searchButton2");
          const countryInput2 = document.getElementById("countryInput2");
          const countryInput3 = document.getElementById("countryInput3");
          const cardTitle2 = document.getElementById("cardTitle2");
      
          searchButton2.addEventListener("click", function() {{
              
              // 根据输入文本进行页面跳转或修改标题颜色
              var countrylist = ['Afghanistan.html', 'Albania.html', 'Algeria.html', 'Andorra.html', 'Angola.html', 'Antarctica.html', 'Antigua & Barbuda.html', 'Argentina.html', 'Armenia.html', 'Australia.html', 'Austria.html', 'Azerbaijan.html', 'Bahamas.html', 'Bahrain.html', 'Bangladesh.html', 'Barbados.html', 'Belgium.html', 'Belize.html', 'Benin.html', 'Bermuda.html', 'Bhutan.html', 'Bolivia.html', 'Bophuthatswana.html', 'Bosnia & Herzegovina.html', 'Botswana.html', 'Brazil.html', 'Brunei.html', 'Bulgaria.html', 'Burkina Faso.html', 'Burma.html', 'Burundi.html', 'Byelarus.html', 'Cambodia.html', 'Cameroon.html', 'Canada.html', 'Cape Verde.html', 'Central African Republic.html', 'Ceylon.html', 'Chad.html', 'Chile.html', 'China.html', 'Ciskei.html', 'Colombia.html', 'Comoros.html', 'Congo.html', 'Cook Islands.html', 'Costa Rica.html', 'Crimea.html', 'Croatia.html', 'Cuba.html', 'Cyprus.html', 'Czech Republic.html', 'Czechoslovakia.html', 'Dahomey.html', 'Democratic Republic of the Congo.html', 'Denmark.html', 'Djibouti.html', 'Dominica .html', 'Dominican Republic.html', 'Ecuador.html', 'Egypt.html', 'El Salvador.html', 'Equatorial Guinea.html', 'Eritrea.html', 'Estonia.html', 'Ethiopia.html', 'Federated States of Micronesia .html', 'Fiji.html', 'Finland.html', 'France.html', 'French-Guiana.html', 'French-Polynesia.html', 'Gabon.html', 'Gambia.html', 'Georgia.html', 'Germany.html', 'Ghana .html', 'Gilbert & Ellice Islands.html', 'Greece.html', 'Grenada.html', 'Guadeloupe.html', 'Guatemala.html', 'Guinea-Bissau.html', 'Guinea.html', 'Guyana.html', 'Haiti.html', 'Honduras .html', 'Hong-Kong.html', 'Hungary.html', 'Iceland.html', 'India.html', 'Indonesia.html', 'Iran.html', 'Iraq.html', 'Ireland.html', 'Israel.html', 'Italy.html', 'Ivory Coast.html', 'Jamaica.html', 'Japan.html', 'Jordan.html', 'Kazakhstan.html', 'Kenya.html', 'Khmer Republic.html', 'Kiribati.html', 'Kuwait.html', 'Kyrgyzstan.html', 'Laos.html', 'Latvia.html', 'Lebanon .html', 'Lesotho.html', 'Liberia .html', 'Libya.html', 'Liechtenstein.html', 'Lithuania.html', 'Luxembourg.html', 'Macau.html', 'Macedonia.html', 'Madagascar.html', 'Malawi.html', 'Malaysia.html', 'Maldives.html', 'Mali.html', 'Malta.html', 'Marshall Islands.html', 'Mauritania.html', 'Mauritius.html', 'Mexico.html', 'Moldova .html', 'Monaco.html', 'Mongolia.html', 'Montenegro.html', 'Morocco.html', 'Mozambique.html', 'Namibia.html', 'Nauru.html', 'Nepal.html', 'Netherlands-Antilles.html', 'Netherlands.html', 'New Zealand.html', 'New-Caledonia.html', 'Nicaragua.html', 'Niger.html', 'Nigeria.html', 'Niue.html', 'North Korea.html', 'Norway.html', 'Oman.html', 'Pakistan.html', 'Palau.html', 'Palestine.html', 'Panama.html', 'Papua New Guinea.html', 'Paraguay.html', "People's Democratic Republic of Yemen.html", "People's Republic of Congo.html", 'Peru.html', 'Philippines.html', 'Poland.html', 'Portugal.html', 'Qatar.html', 'Republic of Kosovo.html', 'Republic of Serbia.html', 'Reunion.html', 'Rhodesia.html', 'Romania.html', 'Russia.html', 'Rwanda.html', 'Saint-Vincent-et-les-Grenadines.html', 'Samoa.html', 'San Marino.html', 'Sao Tome & Principe.html', 'Saudi Arabia.html', 'Senegal.html', 'Senegambia.html', 'Serbia and Montenegro.html', 'Seychelles.html', 'Sierra Leone.html', 'Singapore.html', 'Slovakia.html', 'Slovenia.html', 'Solomon Islands.html', 'Somalia.html', 'South Africa.html', 'South Korea.html', 'South Sudan.html', 'Spain.html', 'Sri Lanka.html', 'St-Kitts & Nevis .html', 'St-Lucia.html', 'Sudan.html', 'Suriname.html', 'Swaziland.html', 'Sweden.html', 'Switzerland.html', 'Syria.html', 'Taiwan.html', 'Tajikistan.html', 'Tanzania.html', 'Thailand.html', 'Togo.html', 'Tonga.html', 'Transkei.html', 'Trinidad and Tobago.html', 'Tunisia.html', 'Turkey.html', 'Turkmenistan.html', 'Tuvalu.html', 'Uganda.html', 'Ukraine.html', 'Union of Soviet Socialist Republics.html', 'United Arab Emirates.html', 'United Arab Republic.html', 'United Kingdom.html', 'United States.html', 'Uruguay.html', 'Uzbekistan.html', 'Vanuatu.html', 'Vatican.html', 'Venda.html', 'Venezuela.html', 'Vietnam.html', 'Western Sahara.html', 'Yemen Arab Republic.html', 'Yemen.html', 'Yugoslavia.html', 'Zaire.html', 'Zambia.html', 'Zimbabwe.html']
              

              if ((!countryInput2.value) || (!countryInput3.value)) {{
                cardTitle2.style.color = "purple";
                cardTitle2.textContent = "抱歉，您未输入需要对比的所有国家或地区。";
              }} else if (countrylist.includes(countryInput2.value+".html") && countrylist.includes(countryInput3.value+".html")) {{
                // 根据文件名进行页面跳转
                localStorage.setItem('country1', countryInput2.value);
                localStorage.setItem('country2', countryInput3.value);
                window.location.href = "../compare.html";
              }} else {{
                cardTitle2.style.color = "purple";
                cardTitle2.textContent = "抱歉，您输入的国家或地区名有误。";
              }}

          }});
      </script>

      </div>
    </section>
    

  </main><!-- End #main -->

  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Vendor JS Files -->
  <script src="../assets/vendor/apexcharts/apexcharts.min.js"></script>
  <script src="../assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../assets/vendor/chart.js/chart.umd.js"></script>
  <script src="../assets/vendor/echarts/echarts.min.js"></script>
  <script src="../assets/vendor/quill/quill.min.js"></script>
  <script src="../assets/vendor/simple-datatables/simple-datatables.js"></script>
  <script src="../assets/vendor/tinymce/tinymce.min.js"></script>
  <script src="../assets/vendor/php-email-form/validate.js"></script>

  <!-- Template Main JS File -->
  <script src="../assets/js/main.js"></script>

</body>

</html>
"""

# Define the directory to save the generated HTML files again
output_dir = "radar charts"
os.makedirs(output_dir, exist_ok=True)

# Extract unique countries from the data (excluding "Unknown")
countries = set(entry['Country'] for entry in data if entry['Country'] != 'Unknown')

# Generate and save the HTML files again with the new features
for country in countries:
    country_specific_data = [entry for entry in data if entry['Country'] == country]
    max_index = len(country_specific_data) - 1
    start_year = country_specific_data[0]['year']
    html_content = html_template.format(country=country, data=country_specific_data, max_index=max_index, start_year=start_year)
    with open(os.path.join(output_dir, f"{country}.html"), 'w', encoding= 'utf-8') as file:
        file.write(html_content)

# Zip the output directory again
shutil.make_archive(output_dir, 'zip', output_dir)