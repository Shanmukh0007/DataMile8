from django.shortcuts import render, redirect
from calc.models import Login
from calc.models import ProjectTable
from calc.models import TeamTable
from django.http import HttpResponse 
from django.db.models import Max

# Now, max_id contains the maximum ID from YourModel



def home(request):
    return render(request, 'home.html')



def signup(request):
    if request.method == 'POST':
        # Form submission logic
        roll_number = request.POST.get('roll_number')
        name = request.POST.get('name')
        year_of_joining = request.POST.get('year_of_joining')
        stream = request.POST.get('stream')
        password=request.POST.get('password')
        
        # Saving to login table
        login_entry = Login(Roll_number=roll_number, Name=name, Year_of_join=year_of_joining, Stream=stream,Password=password)
        login_entry.save()
        # Saving to Teamtable
        team_entry=TeamTable(TeamMembers=roll_number)
        team_entry.save()
        
        
        # Redirect to the success page
        return redirect('success')
    
    #first this block will be executed
    return render(request, 'signup_form.html')





def login(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')

        userinfo=Login.objects.get(Roll_number=roll_number)
        Passinformation=userinfo.Password
        userteaminfo=TeamTable.objects.get(TeamMembers=roll_number)
        
    
        if(password==Passinformation):
            #This sends the information of the person logged in
            max_id=ProjectTable.objects.aggregate(Max('id'))['id__max']
            # Initialize a list to store project data

        
            project_data_list = []

# Loop through projects
            for i in range(1, 3):
                project_from_table = ProjectTable.objects.get(id=i)
                team_from_table = TeamTable.objects.filter(ProjectName=project_from_table.ProjectName)
                first_five_rows = team_from_table[:5]
                members = []
                for row in first_five_rows:
                    members.append(row.TeamMembers)
                
                project_data = {
                    'ProjectName': project_from_table.ProjectName,
                    'ProjectDescription': project_from_table.ProjectDescription,
                    'members': members
                }

                # Append project data to the list
                project_data_list.append(project_data)

            # User information (assuming userinfo, userteaminfo are defined)
            context1 = {
                'Name': userinfo.Name,
                'rollnumber': userinfo.Roll_number,
                'stream': userinfo.Stream,
                'projectname': userteaminfo.ProjectName,
            }

            # Pass the list of project data and user data to the template
            context = {'projects': project_data_list, 'user': context1}
            return render(request, 'interface.html', context)   
        else: 
            return render(request,'try_again_login.html')
    return render(request,'login_form.html')






def createteam(request):
    if request.method == 'POST':
        # Form submission logic
        project_name=request.POST.get('project_name')
        project_description=request.POST.get('project_description')
        team_leader=request.POST.get('team_leader')
        team_member1=request.POST.get('team_member1')
        team_member2=request.POST.get('team_member2')
        team_member3=request.POST.get('team_member3')
        team_member4=request.POST.get('team_member4')
        
        # Saving to the database
        login_entry = ProjectTable(ProjectName=project_name,ProjectDescription=project_description,TeamLeader=team_leader)
        login_entry.save()
        login_entry=TeamTable.objects.filter(TeamMembers=team_leader).update(ProjectName=project_name)
        login_entry=TeamTable.objects.filter(TeamMembers=team_member1).update(ProjectName=project_name)
        login_entry=TeamTable.objects.filter(TeamMembers=team_member2).update(ProjectName=project_name)
        login_entry=TeamTable.objects.filter(TeamMembers=team_member3).update(ProjectName=project_name)
        login_entry=TeamTable.objects.filter(TeamMembers=team_member4).update(ProjectName=project_name)


        
        # Redirect to the success page
        return render(request,'login_form.html')
    
    #first this block will be executed
    return render(request, 'create_team.html')























def success(request):
    # Display the success message
    return render(request, 'success.html', {'message': 'Data saved successfully!'})
