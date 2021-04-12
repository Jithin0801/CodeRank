from django.urls import path
from . import views

urlpatterns = [
    # profile set up
    path("institutions/", views.InsitiutionHomePage,
         name="InsitiutionHomePage"),
    path("institutions/login", views.InstitutionLoginPage,
         name="InstitutionLoginPage"),
    path("institutions/signup", views.InstitutionSignUpPage,
         name="InstitutionSignUpPage"),
    path("institutions/completeprofile", views.InsCompleteProfile,
         name="InsCompleteProfile"),
    path("institutions/myprofile", views.InsMyProfile,
         name="InsMyProfile"),

    # blog
    path("institutions/blogs", views.BlogListPage,
         name="InsBlogListPage"),
    path("institutions/myblogs", views.MyBlogListPage, name="InsMyBlogListPage"),
    path("institutions/newblog", views.PostNewBlog, name="InsPostNewBlog"),
    path("institutions/blogs/<slug:titleslug>",
         views.ViewBlog, name="InsViewBlog"),
    path("institutions/blogs/<slug:titleslug>/edit",
         views.EditBlog, name="InsEditBlog"),
    path("institutions/blogs/user-details/<slug:nameslug>", views.BlogViewUser,
         name="BlogViewUser"),

    # dashboard
    path("institutions/dashboard", views.InsDashboard,
         name="InsDashboard"),

    # problem
    path("institutions/problems", views.ProblemList,
         name="ProblemList"),
    path("institutions/problems/add", views.AddProblem,
         name="AddProblem"),
    path("institutions/problems/<slug:problemslug>", views.ViewProblem,
         name="ViewProblem"),
    path("institutions/problems/<slug:problemslug>/edit", views.EditProblem,
         name="EditProblem"),
    path("institutions/problems/<slug:problemslug>/delete", views.DelProblem,
         name="DelProblem"),

    # main topic curd
    path("institutions/topics/main-topic", views.MainTopicList,
         name="MainTopicList"),
    path("institutions/topics/add-main-topic", views.AddNewMainTopic,
         name="AddNewMainTopic"),
    path("institutions/topics/<slug:maintopic>/edit", views.UpdateMainTopic,
         name="UpdateMainTopic"),
    path("institutions/topics/<slug:maintopic>/delete", views.DelMainTopic,
         name="DelMainTopic"),

    # subtopic curd
    path("institutions/topics/<slug:maintopic>", views.SubTopicList,
         name="SubTopicList"),
    path("institutions/topics/<slug:maintopic>/add-sub-topic", views.AddNewSubTopic,
         name="AddNewSubTopic"),
    path("institutions/topics/<slug:maintopic>/<slug:subtopic>", views.ViewSubTopicContent,
         name="ViewSubTopicContent"),
    path("institutions/topics/<slug:maintopic>/<slug:subtopic>/edit", views.UpdateSubTopic,
         name="UpdateSubTopic"),
    path("institutions/topics/<slug:maintopic>/<slug:subtopic>/delete", views.DelSubTopic,
         name="DelSubTopic"),


    # tutorial
    path("institutions/tutorials", views.InsTutorialsList,
         name="InsTutorialsList"),
    path("institutions/tutorials/add", views.InsAddTutorial,
         name="InsAddTutorial"),
    path("institutions/tutorials/<slug:tutorialsubtopic>/delete", views.InsDelTutorial,
         name="InsDelTutorial"),
    path("institutions/tutorials/<slug:tutorialsubtopic>/edit", views.InsEditTutorial,
         name="InsEditTutorial"),
    path("institutions/tutorials/<slug:tutorialsubtopic>", views.InsViewTutorial,
         name="InsViewTutorial"),

    # competition
    path("institutions/competitions", views.InsCompetitionsList,
         name="InsCompetitionsList"),
    path("institutions/competitions/add", views.InsAddCompetition,
         name="InsAddCompetition"),
    path("institutions/competitions/<slug:competitiontitle>/delete", views.InsDelCompetition,
         name="InsDelCompetition"),
    path("institutions/competitions/<slug:competitiontitle>/edit", views.InsEditCompetition,
         name="InsEditCompetition"),
    path("institutions/competitions/<slug:competitiontitle>/view", views.ViewCompetitionDetails,
         name="ViewCompetitionDetails"),
    path("institutions/competitions/<slug:competitiontitle>/problems/add", views.AddCompetitionProblem,
         name="AddCompetitionProblem"),
    path("institutions/competitions/<slug:competitiontitle>/problems/<slug:problemslug>/edit", views.EditCompetitionProblem,
         name="EditCompetitionProblem"),
    path("institutions/competitions/<slug:competitiontitle>/problems/<slug:problemslug>/delete", views.DelCompetitionProblem,
         name="DelCompetitionProblem"),
    path("institutions/competitions/<slug:competitiontitle>/registered-users", views.ResigteredUsers,
         name="ResigteredUsers"),
    path("institutions/competitions/<slug:competitiontitle>/registered-users/<slug:nameslug>", views.ResultListPage,
         name="ResultListPage"),
    path("institutions/competitions/<slug:competitiontitle>/registered-users/<slug:nameslug>/result/<slug:resultslug>", views.ViewResult,
         name="ViewResult"),
    path("institutions/<slug:nameslug>", views.ViewUser,
         name="ViewUserIns"),
    path("institutions/competitions/<slug:competitiontitle>/registered-users/<slug:nameslug>/delete", views.DelResigteredUser,
         name="DelResigteredUser"),


]
