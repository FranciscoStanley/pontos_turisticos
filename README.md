# pontos_turisticos
## Criando uma api RESTful de pontos turisticos de Brasília, com django RESTframework.

<html lang="pt" class="translated-ltr"><head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta charset="utf-8">
  <title>Home - Django REST framework</title>
  <link href="img/favicon.ico" rel="icon" type="image/x-icon">
  <link rel="canonical" href="https://www.django-rest-framework.org/">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Django, API, REST, Home">
  <meta name="author" content="Tom Christie">

  <!-- Le styles -->
  <link href="css/prettify.css" rel="stylesheet">
  <link href="css/bootstrap.css" rel="stylesheet">
  <link href="css/bootstrap-responsive.css" rel="stylesheet">
  <link href="css/default.css" rel="stylesheet">


  <script type="text/javascript" async="" src="https://ssl.google-analytics.com/ga.js"></script><script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-18852272-2']);
    _gaq.push(['_trackPageview']);

    (function() {
      var ga = document.createElement('script');
      ga.type = 'text/javascript';
      ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0];
      s.parentNode.insertBefore(ga, s);
    })();
  </script>

  <style>
  #sidebarInclude img {
      margin-bottom: 10px;
  }
  #sidebarInclude a.promo {
      color: black;
  }
    @media (max-width: 767px) {
      div.promo {
        display: none;
      }
    }
  </style>
<link type="text/css" rel="stylesheet" charset="UTF-8" href="https://translate.googleapis.com/translate_static/css/translateelement.css"><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script></head>
<body onload="prettyPrint()" class="index-page" cz-shortcut-listen="true">

  <div class="wrapper">
        <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container-fluid">
          <a class="repo-link btn btn-primary btn-small" href="https://github.com/encode/django-rest-framework/tree/master"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">GitHub</font></font></a>
          <a class="repo-link btn btn-inverse btn-small " rel="next" href="tutorial/quickstart/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
            Próximo </font></font><i class="icon-arrow-right icon-white"></i>
          </a>
          <a class="repo-link btn btn-inverse btn-small disabled" rel="prev">
            <i class="icon-arrow-left icon-white"></i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> Anterior
          </font></font></a>
          <a id="search_modal_show" class="repo-link btn btn-inverse btn-small" href="#mkdocs_search_modal" data-toggle="modal" data-target="#mkdocs_search_modal"><i class="icon-search icon-white"></i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> Procurar</font></font></a>
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="https://www.django-rest-framework.org/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Framework Django REST</font></font></a>
          <div class="nav-collapse collapse">
            
            <!-- Main navigation -->
            <ul class="nav navbar-nav">
               
              <li class="active">
                <a href="."><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Casa</font></font></a>
              </li>
                
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tutorial </font></font><b class="caret"></b></a>
                <ul class="dropdown-menu" style="max-height: 506px;">
                  
                  <li>
                    <a href="tutorial/quickstart/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Começo rápido</font></font></a>
                  </li>
                  
                  <li>
                    <a href="tutorial/1-serialization/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">1 - Serialização</font></font></a>
                  </li>
                  
                  <li>
                    <a href="tutorial/2-requests-and-responses/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2 - Solicitações e respostas</font></font></a>
                  </li>
                  
                  <li>
                    <a href="tutorial/3-class-based-views/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3 - Visualizações baseadas em classe</font></font></a>
                  </li>
                  
                  <li>
                    <a href="tutorial/4-authentication-and-permissions/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">4 - Autenticação e permissões</font></font></a>
                  </li>
                  
                  <li>
                    <a href="tutorial/5-relationships-and-hyperlinked-apis/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">5 - Relacionamentos e APIs com hiperlinks</font></font></a>
                  </li>
                  
                  <li>
                    <a href="tutorial/6-viewsets-and-routers/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">6 - Viewsets e roteadores</font></font></a>
                  </li>
                  
                </ul>
              </li>
                
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Guia de API </font></font><b class="caret"></b></a>
                <ul class="dropdown-menu" style="max-height: 506px;">
                  
                  <li>
                    <a href="api-guide/requests/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">solicitações de</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/responses/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Respostas</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/views/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Visualizações</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/generic-views/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Vistas genéricas</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/viewsets/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Conjuntos de visualizações</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/routers/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Roteadores</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/parsers/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Analisadores</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/renderers/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Renderers</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/serializers/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Serializadores</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/fields/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Campos do serializador</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/relations/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Relações do serializador</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/validators/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Validadores</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/authentication/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Autenticação</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/permissions/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Permissões</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/caching/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Cache</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/throttling/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Estrangulamento</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/filtering/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Filtrando</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/pagination/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Paginação</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/versioning/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Controle de versão</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/content-negotiation/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Negociação de conteúdo</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/metadata/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Metadados</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/schemas/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Esquemas</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/format-suffixes/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sufixos de formato</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/reverse/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Retornando URLs</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/exceptions/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Exceções</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/status-codes/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Códigos de status</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/testing/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Testando</font></font></a>
                  </li>
                  
                  <li>
                    <a href="api-guide/settings/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Definições</font></font></a>
                  </li>
                  
                </ul>
              </li>
                
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tópicos </font></font><b class="caret"></b></a>
                <ul class="dropdown-menu" style="max-height: 506px;">
                  
                  <li>
                    <a href="topics/documenting-your-api/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Documentando sua API</font></font></a>
                  </li>
                  
                  <li>
                    <a href="topics/api-clients/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Clientes API</font></font></a>
                  </li>
                  
                  <li>
                    <a href="topics/internationalization/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Internacionalização</font></font></a>
                  </li>
                  
                  <li>
                    <a href="topics/ajax-csrf-cors/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">AJAX, CSRF e CORS</font></font></a>
                  </li>
                  
                  <li>
                    <a href="topics/html-and-forms/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML e formulários</font></font></a>
                  </li>
                  
                  <li>
                    <a href="topics/browser-enhancements/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aprimoramentos do navegador</font></font></a>
                  </li>
                  
                  <li>
                    <a href="topics/browsable-api/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A API Browsable</font></font></a>
                  </li>
                  
                  <li>
                    <a href="topics/rest-hypermedia-hateoas/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">REST, hipermídia e ódio</font></font></a>
                  </li>
                  
                </ul>
              </li>
                
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Comunidade </font></font><b class="caret"></b></a>
                <ul class="dropdown-menu" style="max-height: 506px;">
                  
                  <li>
                    <a href="community/tutorials-and-resources/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tutoriais e recursos</font></font></a>
                  </li>
                  
                  <li>
                    <a href="community/third-party-packages/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Pacotes de Terceiros</font></font></a>
                  </li>
                  
                  <li>
                    <a href="community/contributing/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Contribuindo para a estrutura REST</font></font></a>
                  </li>
                  
                  <li>
                    <a href="community/project-management/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Gerenciamento de Projetos</font></font></a>
                  </li>
                  
                  <li>
                    <a href="community/release-notes/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Notas de Lançamento</font></font></a>
                  </li>
                  
                  <li>
                    <a href="community/3.12-announcement/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.12 Anúncio</font></font></a>
                  </li>
                  
                  <li>
                    <a href="community/3.11-announcement/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.11 Anúncio</font></font></a>
                  </li>
                  
                  <li>
                    <a href="community/3.10-announcement/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.10 Anúncio</font></font></a>
                  </li>
                  
                  <li>
                    <a href="community/3.9-announcement/">3.9 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.8-announcement/">3.8 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.7-announcement/">3.7 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.6-announcement/">3.6 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.5-announcement/">3.5 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.4-announcement/">3.4 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.3-announcement/">3.3 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.2-announcement/">3.2 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.1-announcement/">3.1 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/3.0-announcement/">3.0 Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/kickstarter-announcement/">Kickstarter Announcement</a>
                  </li>
                  
                  <li>
                    <a href="community/mozilla-grant/">Mozilla Grant</a>
                  </li>
                  
                  <li>
                    <a href="community/funding/">Funding</a>
                  </li>
                  
                  <li>
                    <a href="community/jobs/">Jobs</a>
                  </li>
                  
                </ul>
              </li>
               

            </ul>
            
          </div>
          <!--/.nav-collapse -->

        </div>
      </div>
    </div>

    <div class="body-content">
      <div class="container-fluid">
        <!-- Search Modal -->
        <div id="mkdocs_search_modal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h3 id="myModalLabel">Documentation search</h3>
          </div>

          <div class="modal-body">
            <form role="form" autocomplete="off">
              <div class="form-group">
                <input type="text" name="q" class="form-control" placeholder="Search..." id="mkdocs-search-query">
              </div>
            </form>
            <div id="mkdocs-search-results"></div>
          </div>

          <div class="modal-footer">
            <button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
          </div>
        </div>

        <div class="row-fluid">
          <div class="span3">
            <div id="table-of-contents">
              <ul class="nav nav-list side-nav well sidebar-nav-fixed" style="max-height: 506px;">
                
                  <li class="main">
                    <a href="#"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Framework Django REST</font></font></a>
                  </li>
                

                
                  <li class="">
                    <a href="#funding"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Financiamento</font></font></a>
                  </li>

                  
                
                  <li class="">
                    <a href="#requirements"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisitos</font></font></a>
                  </li>

                  
                
                  <li class="">
                    <a href="#installation"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Instalação</font></font></a>
                  </li>

                  
                
                  <li class="">
                    <a href="#example"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Exemplo</font></font></a>
                  </li>

                  
                
                  <li class="">
                    <a href="#quickstart"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Começo rápido</font></font></a>
                  </li>

                  
                
                  <li class="">
                    <a href="#development"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Desenvolvimento</font></font></a>
                  </li>

                  
                
                  <li class="">
                    <a href="#support"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apoio, suporte</font></font></a>
                  </li>

                  
                
                  <li class="">
                    <a href="#security"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segurança</font></font></a>
                  </li>

                  
                
                  <li class="">
                    <a href="#license"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Licença</font></font></a>
                  </li>

                  
                

                  <div class="promo">
                    <hr>
                    <div id="sidebarInclude"><a href="http://www.ismltd.com"><img width="130px" src="https://fund-rest-framework.s3.amazonaws.com/ism_games.png"></a><p><a class="promo" href="http://www.ismltd.com"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ISM Fantasy Games - Nós projetamos, desenvolvemos e operamos jogos de fantasy sports em grande escala.</font></font></a></p><p><a href="https://fund.django-rest-framework.org/topics/funding/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Estrutura Django REST do fundo</font></font></a></p></div>
              </div></ul>

            </div>
          </div>

          <div id="main-content" class="span9">
            
              

              <style>
.promo li a {
    float: left;
    width: 130px;
    height: 20px;
    text-align: center;
    margin: 10px 30px;
    padding: 150px 0 0 0;
    background-position: 0 50%;
    background-size: 130px auto;
    background-repeat: no-repeat;
    font-size: 120%;
    color: black;
}
.promo li {
    list-style: none;
}
</style>

<p class="badges" height="20px">
    <iframe src="https://ghbtns.com/github-btn.html?user=encode&amp;repo=django-rest-framework&amp;type=watch&amp;count=true" class="github-star-button" allowtransparency="true" frameborder="0" scrolling="0" width="110px" height="20px"></iframe>

    <a href="https://github.com/encode/django-rest-framework/actions/workflows/main.yml">
        <img src="https://github.com/encode/django-rest-framework/actions/workflows/main.yml/badge.svg" class="status-badge">
    </a>

    <a href="https://pypi.org/project/djangorestframework/">
        <img src="https://img.shields.io/pypi/v/djangorestframework.svg" class="status-badge">
    </a>
</p>

<hr>
<p>
</p><h1 style="position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0,0,0,0);
    border: 0;"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Django REST Framework</font></font></h1>

<img alt="Django REST Framework" title="Logotipo de Jake 'Sid' Smith" src="img/logo.png" width="600px" style="display: block; margin: 0 auto 0 auto">
<p></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A estrutura Django REST é um kit de ferramentas poderoso e flexível para a construção de APIs da Web.</font></font></p>
<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Alguns motivos pelos quais você pode querer usar a estrutura REST:</font></font></p>
<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A </font></font><a href="https://restframework.herokuapp.com/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">API navegável da Web</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> é uma grande vitória de usabilidade para seus desenvolvedores.</font></font></li>
<li><a href="api-guide/authentication/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Políticas de autenticação,</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> incluindo pacotes para </font></font><a href="api-guide/authentication/#django-rest-framework-oauth"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">OAuth1a</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> e </font></font><a href="api-guide/authentication/#django-oauth-toolkit"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">OAuth2</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> .</font></font></li>
<li><a href="api-guide/serializers/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Serialização</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> que suporta </font><font style="vertical-align: inherit;">fontes de dados </font></font><a href="api-guide/serializers#modelserializer"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ORM</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> e </font></font><a href="api-guide/serializers#serializers"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">não ORM</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> .</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Totalmente personalizável - basta usar </font></font><a href="api-guide/views#function-based-views"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">visualizações regulares baseadas em função</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> se você não precisar de </font><a href="api-guide/routers/"><font style="vertical-align: inherit;">recursos </font></a></font><a href="api-guide/generic-views/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">mais </font></font></a> <a href="api-guide/viewsets/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">poderosos</font></font></a> <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> .</font></font><a href="api-guide/routers/"><font style="vertical-align: inherit;"></font></a><font style="vertical-align: inherit;"></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Documentação extensa e </font></font><a href="https://groups.google.com/forum/?fromgroups#!forum/django-rest-framework"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ótimo suporte da comunidade</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> .</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usado e confiado por empresas internacionalmente reconhecidas, incluindo </font></font><a href="https://www.mozilla.org/en-US/about/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Mozilla</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> , </font></font><a href="https://www.redhat.com/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Red Hat</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> , </font></font><a href="https://www.heroku.com/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Heroku</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> e </font></font><a href="https://www.eventbrite.co.uk/about/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Eventbrite</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> .</font></font></li>
</ul>
<hr>
<h2 id="funding"><a class="toclink" href="#funding"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Financiamento</font></font></a></h2>
<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O framework REST é um </font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">projeto financiado de forma colaborativa</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> . </font><font style="vertical-align: inherit;">Se você usa a estrutura REST comercialmente, recomendamos fortemente que você invista em seu desenvolvimento contínuo, </font></font><strong><a href="community/funding/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">inscrevendo-se em um plano pago</font></font></a></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> .</font></font></p>
<p><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Cada inscrição nos ajuda a tornar a estrutura REST financeiramente sustentável a longo prazo.</font></font></em></p>
<ul class="premium-promo promo">
    <li><a href="https://getsentry.com/welcome/" style="background-image: url(https://fund-rest-framework.s3.amazonaws.com/sentry130.png)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sentinela</font></font></a></li>
    <li><a href="https://getstream.io/?utm_source=drf&amp;utm_medium=sponsorship&amp;utm_content=developer" style="background-image: url(https://fund-rest-framework.s3.amazonaws.com/stream-130.png)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Stream</font></font></a></li>
    <li><a href="https://software.esg-usa.com" style="background-image: url(https://fund-rest-framework.s3.amazonaws.com/esg-new-logo.png)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ESG</font></font></a></li>
    <li><a href="https://rollbar.com" style="background-image: url(https://fund-rest-framework.s3.amazonaws.com/rollbar2.png)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Rollbar</font></font></a></li>
    <li><a href="https://retool.com/?utm_source=djangorest&amp;utm_medium=sponsorship" style="background-image: url(https://fund-rest-framework.s3.amazonaws.com/retool-sidebar.png)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Retool</font></font></a></li>
    <li><a href="https://bit.io/jobs?utm_source=DRF&amp;utm_medium=sponsor&amp;utm_campaign=DRF_sponsorship" style="background-image: url(https://fund-rest-framework.s3.amazonaws.com/bitio_logo_gold_background.png)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">bit.io</font></font></a></li>
</ul>
<div style="clear: both; padding-bottom: 20px;"></div>

<p><em>Many thanks to all our <a href="https://fund.django-rest-framework.org/topics/funding/#our-sponsors">wonderful sponsors</a>, and in particular to our premium backers, <a href="https://getsentry.com/welcome/">Sentry</a>, <a href="https://getstream.io/?utm_source=drf&amp;utm_medium=sponsorship&amp;utm_content=developer">Stream</a>, <a href="https://software.esg-usa.com/">ESG</a>, <a href="https://rollbar.com/?utm_source=django&amp;utm_medium=sponsorship&amp;utm_campaign=freetrial">Rollbar</a>, <a href="https://cadre.com">Cadre</a>, <a href="https://hubs.ly/H0f30Lf0">Kloudless</a>, <a href="https://lightsonsoftware.com">Lights On Software</a>, <a href="https://retool.com/?utm_source=djangorest&amp;utm_medium=sponsorship">Retool</a>, and <a href="https://bit.io/jobs?utm_source=DRF&amp;utm_medium=sponsor&amp;utm_campaign=DRF_sponsorship">bit.io</a>.</em></p>
<hr>
<h2 id="requirements"><a class="toclink" href="#requirements">Requirements</a></h2>
<p>REST framework requires the following:</p>
<ul>
<li>Python (3.5, 3.6, 3.7, 3.8, 3.9)</li>
<li>Django (2.2, 3.0, 3.1, 3.2)</li>
</ul>
<p>We <strong>highly recommend</strong> and only officially support the latest patch release of
each Python and Django series.</p>
<p>The following packages are optional:</p>
<ul>
<li><a href="https://pypi.org/project/PyYAML/">PyYAML</a>, <a href="https://pypi.org/project/uritemplate/">uritemplate</a> (5.1+, 3.0.0+) - Schema generation support.</li>
<li><a href="https://pypi.org/project/Markdown/">Markdown</a> (3.0.0+) - Markdown support for the browsable API.</li>
<li><a href="https://pypi.org/project/Pygments/">Pygments</a> (2.4.0+) - Add syntax highlighting to Markdown processing.</li>
<li><a href="https://pypi.org/project/django-filter/">django-filter</a> (1.0.1+) - Filtering support.</li>
<li><a href="https://github.com/django-guardian/django-guardian">django-guardian</a> (1.1.1+) - Object level permissions support.</li>
</ul>
<h2 id="installation"><a class="toclink" href="#installation">Installation</a></h2>
<p>Install using <code>pip</code>, including any optional packages you want...</p>
<pre class="prettyprint well"><code><span class="pln">pip install djangorestframework</span><font></font><span class="pln">
pip install markdown       </span><span class="com"># Markdown support for the browsable API.</span><font></font><span class="pln">
pip install django</span><span class="pun">-</span><span class="pln">filter  </span><span class="com"># Filtering support</span><font></font>
</code></pre>
<p>...or clone the project from github.</p>
<pre class="prettyprint well"><code><span class="pln">git clone https</span><span class="pun">:</span><span class="com">//github.com/encode/django-rest-framework</span></code></pre>
<p>Add <code>'rest_framework'</code> to your <code>INSTALLED_APPS</code> setting.</p>
<pre class="prettyprint well"><code><span class="pln">INSTALLED_APPS </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><font></font><span class="pln">
    </span><span class="pun">...</span><font></font><span class="pln">
    </span><span class="str">'rest_framework'</span><span class="pun">,</span><font></font><span class="pln">
</span><span class="pun">]</span><font></font>
</code></pre>
<p>If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views.  Add the following to your root <code>urls.py</code> file.</p>
<pre class="prettyprint well"><code><span class="pln">urlpatterns </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><font></font><span class="pln">
    </span><span class="pun">...</span><font></font><span class="pln">
    path</span><span class="pun">(</span><span class="str">'api-auth/'</span><span class="pun">,</span><span class="pln"> include</span><span class="pun">(</span><span class="str">'rest_framework.urls'</span><span class="pun">))</span><font></font><span class="pln">
</span><span class="pun">]</span><font></font>
</code></pre>
<p>Note that the URL path can be whatever you want.</p>
<h2 id="example"><a class="toclink" href="#example">Example</a></h2>
<p>Let's take a look at a quick example of using REST framework to build a simple model-backed API.</p>
<p>We'll create a read-write API for accessing information on the users of our project.</p>
<p>Any global settings for a REST framework API are kept in a single configuration dictionary named <code>REST_FRAMEWORK</code>.  Start off by adding the following to your <code>settings.py</code> module:</p>
<pre class="prettyprint well"><code><span class="pln">REST_FRAMEWORK </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><font></font><span class="pln">
    </span><span class="com"># Use Django's standard `django.contrib.auth` permissions,</span><font></font><span class="pln">
    </span><span class="com"># or allow read-only access for unauthenticated users.</span><font></font><span class="pln">
    </span><span class="str">'DEFAULT_PERMISSION_CLASSES'</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[</span><font></font><span class="pln">
        </span><span class="str">'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'</span><font></font><span class="pln">
    </span><span class="pun">]</span><font></font><span class="pln">
</span><span class="pun">}</span><font></font>
</code></pre>
<p>Don't forget to make sure you've also added <code>rest_framework</code> to your <code>INSTALLED_APPS</code>.</p>
<p>We're ready to create our API now.
Here's our project's root <code>urls.py</code> module:</p>
<pre class="prettyprint well"><code><span class="kwd">from</span><span class="pln"> django</span><span class="pun">.</span><span class="pln">urls </span><span class="kwd">import</span><span class="pln"> path</span><span class="pun">,</span><span class="pln"> include</span><font></font><span class="pln">
</span><span class="kwd">from</span><span class="pln"> django</span><span class="pun">.</span><span class="pln">contrib</span><span class="pun">.</span><span class="pln">auth</span><span class="pun">.</span><span class="pln">models </span><span class="kwd">import</span><span class="pln"> </span><span class="typ">User</span><font></font><span class="pln">
</span><span class="kwd">from</span><span class="pln"> rest_framework </span><span class="kwd">import</span><span class="pln"> routers</span><span class="pun">,</span><span class="pln"> serializers</span><span class="pun">,</span><span class="pln"> viewsets</span><font></font><span class="pln">
</span><font></font><span class="pln">
</span><span class="com"># Serializers define the API representation.</span><font></font><span class="pln">
</span><span class="kwd">class</span><span class="pln"> </span><span class="typ">UserSerializer</span><span class="pun">(</span><span class="pln">serializers</span><span class="pun">.</span><span class="typ">HyperlinkedModelSerializer</span><span class="pun">):</span><font></font><span class="pln">
    </span><span class="kwd">class</span><span class="pln"> </span><span class="typ">Meta</span><span class="pun">:</span><font></font><span class="pln">
        model </span><span class="pun">=</span><span class="pln"> </span><span class="typ">User</span><font></font><span class="pln">
        fields </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'url'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'username'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'email'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'is_staff'</span><span class="pun">]</span><font></font><span class="pln">
</span><font></font><span class="pln">
</span><span class="com"># ViewSets define the view behavior.</span><font></font><span class="pln">
</span><span class="kwd">class</span><span class="pln"> </span><span class="typ">UserViewSet</span><span class="pun">(</span><span class="pln">viewsets</span><span class="pun">.</span><span class="typ">ModelViewSet</span><span class="pun">):</span><font></font><span class="pln">
    queryset </span><span class="pun">=</span><span class="pln"> </span><span class="typ">User</span><span class="pun">.</span><span class="pln">objects</span><span class="pun">.</span><span class="pln">all</span><span class="pun">()</span><font></font><span class="pln">
    serializer_class </span><span class="pun">=</span><span class="pln"> </span><span class="typ">UserSerializer</span><font></font><span class="pln">
</span><font></font><span class="pln">
</span><span class="com"># Routers provide an easy way of automatically determining the URL conf.</span><font></font><span class="pln">
router </span><span class="pun">=</span><span class="pln"> routers</span><span class="pun">.</span><span class="typ">DefaultRouter</span><span class="pun">()</span><font></font><span class="pln">
router</span><span class="pun">.</span><span class="kwd">register</span><span class="pun">(</span><span class="pln">r</span><span class="str">'users'</span><span class="pun">,</span><span class="pln"> </span><span class="typ">UserViewSet</span><span class="pun">)</span><font></font><span class="pln">
</span><font></font><span class="pln">
</span><span class="com"># Wire up our API using automatic URL routing.</span><font></font><span class="pln">
</span><span class="com"># Additionally, we include login URLs for the browsable API.</span><font></font><span class="pln">
urlpatterns </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><font></font><span class="pln">
    path</span><span class="pun">(</span><span class="str">''</span><span class="pun">,</span><span class="pln"> include</span><span class="pun">(</span><span class="pln">router</span><span class="pun">.</span><span class="pln">urls</span><span class="pun">)),</span><font></font><span class="pln">
    path</span><span class="pun">(</span><span class="str">'api-auth/'</span><span class="pun">,</span><span class="pln"> include</span><span class="pun">(</span><span class="str">'rest_framework.urls'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">namespace</span><span class="pun">=</span><span class="str">'rest_framework'</span><span class="pun">))</span><font></font><span class="pln">
</span><span class="pun">]</span><font></font>
</code></pre>
<p>You can now open the API in your browser at <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>, and view your new 'users' API. If you use the login control in the top right corner you'll also be able to add, create and delete users from the system.</p>
<h2 id="quickstart"><a class="toclink" href="#quickstart">Quickstart</a></h2>
<p>Can't wait to get started? The <a href="tutorial/quickstart/">quickstart guide</a> is the fastest way to get up and running, and building APIs with REST framework.</p>
<h2 id="development"><a class="toclink" href="#development">Development</a></h2>
<p>See the <a href="community/contributing/">Contribution guidelines</a> for information on how to clone
the repository, run the test suite and contribute changes back to REST
Framework.</p>
<h2 id="support"><a class="toclink" href="#support">Support</a></h2>
<p>For support please see the <a href="https://groups.google.com/forum/?fromgroups#!forum/django-rest-framework">REST framework discussion group</a>, try the  <code>#restframework</code> channel on <code>irc.libera.chat</code>, or raise a  question on <a href="https://stackoverflow.com/">Stack Overflow</a>, making sure to include the <a href="https://stackoverflow.com/questions/tagged/django-rest-framework">'django-rest-framework'</a> tag.</p>
<p>For priority support please sign up for a <a href="https://fund.django-rest-framework.org/topics/funding/">professional or premium sponsorship plan</a>.</p>
<h2 id="security"><a class="toclink" href="#security">Security</a></h2>
<p>If you believe you’ve found something in Django REST framework which has security implications, please <strong>do not raise the issue in a public forum</strong>.</p>
<p>Send a description of the issue via email to <a href="mailto:rest-framework-security@googlegroups.com">rest-framework-security@googlegroups.com</a>.  The project maintainers will then work with you to resolve any issues where required, prior to any public disclosure.</p>
<h2 id="license"><a class="toclink" href="#license">License</a></h2>
<p>Copyright © 2011-present, <a href="https://www.encode.io/">Encode OSS Ltd</a>.
All rights reserved.</p>
<p>Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:</p>
<ul>
<li>
<p>Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.</p>
</li>
<li>
<p>Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.</p>
</li>
<li>
<p>Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.</p>
</li>
</ul>
<p>THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
            

          </div> <!--/span-->
        </div> <!--/row-->
      </div> <!--/.fluid-container-->
    </div> <!--/.body content-->
    <div id="push"></div>
  </div> <!--/.wrapper -->

  <footer class="span12">
    <p>Documentation built with <a href="http://www.mkdocs.org/">MkDocs</a>.
    </p>
  </footer>

  <!-- Le javascript
  ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script async="" src="https://fund.django-rest-framework.org/sidebar_include.js"></script>
  <script src="js/jquery-1.8.1-min.js"></script>
  <script src="js/prettify-1.0.js"></script>
  <script src="js/bootstrap-2.1.1-min.js"></script>
  <script src="js/theme.js"></script>

  <script>var base_url = '.';</script>
  
  <script src="search/main.js" defer=""></script>
  

  <script>
    var shiftWindow = function() {
      scrollBy(0, -50)
    };

    if (location.hash) shiftWindow();
    window.addEventListener("hashchange", shiftWindow);

    $('.dropdown-menu').on('click touchstart', function(event) {
      event.stopPropagation();
    });

    // Dynamically force sidenav/dropdown to no higher than browser window
    $('.side-nav, .dropdown-menu').css('max-height', window.innerHeight - 130);

    $(function() {
      $(window).resize(function() {
        $('.side-nav, .dropdown-menu').css('max-height', window.innerHeight - 130);
      });
    });
  </script><div id="goog-gt-tt" class="skiptranslate" dir="ltr"><div style="padding: 8px;"><div><div class="logo"><img src="https://www.gstatic.com/images/branding/product/1x/translate_24dp.png" width="20" height="20" alt="Google Tradutor"></div></div></div><div class="top" style="padding: 8px; float: left; width: 100%;"><h1 class="title gray">Texto original</h1></div><div class="middle" style="padding: 8px;"><div class="original-text"></div></div><div class="bottom" style="padding: 8px;"><div class="activity-links"><span class="activity-link">Sugerir uma tradução melhor</span><span class="activity-link"></span></div><div class="started-activity-container"><hr style="color: #CCC; background-color: #CCC; height: 1px; border: none;"><div class="activity-root"></div></div></div><div class="status-message" style="display: none;"></div></div>


<div class="goog-te-spinner-pos"><div class="goog-te-spinner-animation"><svg xmlns="http://www.w3.org/2000/svg" class="goog-te-spinner" width="96px" height="96px" viewBox="0 0 66 66"><circle class="goog-te-spinner-path" fill="none" stroke-width="6" stroke-linecap="round" cx="33" cy="33" r="30"></circle></svg></div></div></body></html>

