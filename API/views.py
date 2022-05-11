from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UsersSerializer, UserSerializer, AgainstUsersSerializer, ReviewerUsersSerializer, ComplaintSerializer
from Authentication.models import CustomUser
from Complaint.models import History


# returns all the users in db
@api_view(['GET'])
def getUsers(request):
    users = CustomUser.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


# returns a single user from db
@api_view(['GET'])
def getUser(request, pk):
    user = CustomUser.objects.get(email=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getReview(request):
    users = get_user_model().objects.all().exclude(email=request.user.email).exclude(type='Student').exclude(
        type='Staff')
    serializer = ReviewerUsersSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAgainst(request):
    users = get_user_model().objects.all().exclude(email=request.user.email).exclude(
        email='projectwork.testemail@gmail.com')
    serializer = AgainstUsersSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addComplaint(request):
    complaint = request.data
    # if str(complaint.against) == str(request.user.email):
    #     return Response({'status': 'Failed!', 'message': 'You cannot complain against yourself!'})
    # elif str(complaint.reviewer) == str(request.user.email):
    #     return Response({'status': 'Failed!', 'message': 'You cannot review your own complaint!'})
    # else:
    #     complaint.user = request.user
    #     complaint.status = 'Submitted'
    #     if complaint.reviewer is None:
    #         complaint.reviewer = get_user_model().objects.get(email='projectwork.testemail@gmail.com')
    #     user_reviewer = get_user_model().objects.get(email=complaint.reviewer)
    #     user_against = get_user_model().objects.get(email=complaint.against)
    #     if complaint.against_2 is None and complaint.against_3 is not None:
    #         return Response({'status': 'Failed!', 'message': 'Please select first two fields if complaining against two people!'})
    #     else:
    #         if complaint.against_2 is not None:
    #             user_against2 = get_user_model().objects.get(email=complaint.against_2)
    #             if user_against2 == user_against:
    #                 return Response({'status': 'Failed!', 'message': 'You cannot select same person multiple times to complaint against!'})
    #         if complaint.against_3 is not None:
    #             user_against3 = get_user_model().objects.get(email=complaint.against_3)
    #             if user_against2 == user_against3 or user_against3 == user_against:
    #                 return Response({'status': 'Failed!', 'message': 'You cannot select same person multiple times to complaint against!'})
    #         complaint.save()
    #         history = History.objects.create(
    #             complaint_id=complaint,
    #             reviewer=complaint.reviewer,
    #             text=complaint.complaint_text,
    #             status=complaint.status,
    #         )
    #         subject = 'Complaint Created!'
    #         if user_reviewer.email != 'projectwork.testemail@gmail.com':
    #             body = 'Hello System Admin, ' + ', a complaint against ' + str(
    #                 user_against.name) + ' has been submitted by ' + str(request.user.name) + '.'
    #             send_mail(
    #                 subject,
    #                 body,
    #                 settings.EMAIL_HOST_USER,
    #                 ['projectwork.testemail@gmail.com'],
    #                 fail_silently=False,
    #             )
    #         names = str(user_against.name)
    #         if complaint.against_2 is not None:
    #             names += ', '
    #             names += str(user_against2.name)
    #         if complaint.against_3 is not None:
    #             names += ', '
    #             names += str(user_against3.name)
    #         body = 'Hello ' + str(
    #             request.user.name) + ', your complaint against ' + names + ' has been submitted successfully.'
    #         send_mail(
    #             subject,
    #             body,
    #             settings.EMAIL_HOST_USER,
    #             [request.user.email],
    #             fail_silently=False,
    #         )
    #         body = 'Hello ' + str(user_reviewer.name) + ', a complaint has been lodged for you to review.'
    #         send_mail(
    #             subject,
    #             body,
    #             settings.EMAIL_HOST_USER,
    #             [user_reviewer.email],
    #             fail_silently=False,
    #         )
    #         return Response({'status': 'OK', 'message': 'Your Complaint was submitted Successfully!'})
    serializer = ComplaintSerializer(complaint, many=False)
    return Response(serializer.data)
