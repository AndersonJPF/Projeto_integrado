from django.db import models

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    pergunta = models.CharField(max_length=100)
    resposta = models.CharField(max_length=100)
    nivel = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pergunta

    def move(self, solved):
        new_box = self.nivel + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.nivel = new_box
            self.save()

        return self
