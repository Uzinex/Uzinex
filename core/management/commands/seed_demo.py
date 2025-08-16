from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from marketplace.models import Project, Proposal, Contract
from messaging.models import Thread, Message
from payments.models import Transaction


class Command(BaseCommand):
    """Seed the database with demo data."""

    def handle(self, *args, **options):
        User = get_user_model()
        Transaction.objects.all().delete()
        Message.objects.all().delete()
        Thread.objects.all().delete()
        Contract.objects.all().delete()
        Proposal.objects.all().delete()
        Project.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        clients = [
            User.objects.create_user(username=f"client{i}", email=f"c{i}@x.com", password="password123", role="client")
            for i in range(1, 3)
        ]
        freelancers = [
            User.objects.create_user(username=f"freelancer{i}", email=f"f{i}@x.com", password="password123", role="freelancer")
            for i in range(1, 4)
        ]

        projects = []
        for i in range(1, 6):
            client = clients[i % 2]
            project = Project.objects.create(
                client=client,
                title=f"Project {i}",
                description="Demo project",
                skills=["Python", "Django"] if i % 2 == 0 else ["React", "UI"],
                budget_min=100 * i,
                budget_max=200 * i,
            )
            projects.append(project)
            for fr in freelancers[:3]:
                Proposal.objects.create(
                    project=project,
                    freelancer=fr,
                    cover_letter="I can do it",
                    bid_amount=150 * i,
                    eta_days=7 + i,
                )

        proposal = projects[0].proposals.first()
        contract = Contract.objects.create(project=projects[0], proposal=proposal)
        projects[0].status = "in_progress"
        projects[0].save(update_fields=["status"])
        proposal.status = "accepted"
        proposal.save(update_fields=["status"])
        Proposal.objects.filter(project=projects[0]).exclude(id=proposal.id).update(status="rejected")

        thread = Thread.objects.create(project=projects[0])
        thread.participants.set([projects[0].client, proposal.freelancer])
        Message.objects.create(thread=thread, sender=projects[0].client, body="Hello")
        Message.objects.create(thread=thread, sender=proposal.freelancer, body="Hi")

        Transaction.objects.create(contract=contract, amount=1000)

        self.stdout.write(self.style.SUCCESS("Demo data created"))
