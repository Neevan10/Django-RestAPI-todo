from rest_framework import serializers
from .models import Todo
class TodoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id","task", "completed", "timestamp", "updated", "user"]

    def validate_completed(self, value):
        #completed = self.initial_data.get('completed') if self.initial_data else None
        #if value is False:
        #    if 'completed' in self.initial_data and self.initial_data['completed'] is False:
        #        raise serializers.ValidationError("Once marked as completed, it can't be changed back to incomplete!")
        #return value
        if self.instance:
            if self.instance.completed and not value:
                raise serializers.ValidationError("Once marked as completed, it can't be changed back to incomplete!")
        #elif value is False:  
        #    raise serializers.ValidationError("New tasks cannot be marked as incomplete initially.")
        return value