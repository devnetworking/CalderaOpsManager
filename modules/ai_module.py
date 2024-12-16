import yaml
import openai
from openai.error import OpenAIError
from datetime import datetime
import re

class AIEngine:
    def __init__(self, config_path):
        """Initialise AIEngine avec la configuration provenant du fichier YAML"""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        self.openai_api_key = config['OPENAI_API_KEY']
        openai.api_key = self.openai_api_key
    
    def generate_bug_recommendations(self, operation_results):
        """Génère des recommandations basées sur les résultats des opérations avec le statut "success"."""
        try:
            # Filtrez les opérations qui ont le statut "success"
            successful_results = [
                {'id': op.get('id'), 'status': op.get('status'), 'name': op.get('name')} 
                for op in operation_results if op.get('status') == 'success'
            ]
            filtered_results = successful_results[:5]  # Limitez à 5 résultats pour éviter de dépasser la limite de tokens
            prompt = f"Provide specific Ansible playbook tasks to remediate the following vulnerabilities: {filtered_results}. Only include executable shell commands with no extra explanation."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI assistant that provides Ansible playbook tasks for vulnerability remediation."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                n=1,
                temperature=0.7
            )
            return response.choices[0].message['content'].strip()
        except OpenAIError as e:
            raise Exception(f"Failed to generate recommendations: {e}")
    
    def extract_shell_commands(self, recommendations):
        """Extrait uniquement les vraies commandes shell des recommandations."""
        commands = []
        
        # Exemple de regex pour identifier les commandes shell valides
        command_patterns = [
            r'\b(apt-get|yum|systemctl|docker|reboot|echo|cp|mv|chmod|chown|ansible-playbook)\b.*'
        ]

        for line in recommendations.split('\n'):
            line = line.strip()
            if any(re.match(pattern, line) for pattern in command_patterns):
                commands.append(line)
        
        return commands

    def generate_ansible_playbook(self, recommendations):
        """Génère un playbook Ansible basé sur les recommandations fournies."""
        try:
            # Extrait uniquement les commandes shell valides
            commands = self.extract_shell_commands(recommendations)
            
            if not commands:
                raise Exception("No valid shell commands found in the recommendations.")
            
            tasks = []
            for idx, command in enumerate(commands):
                tasks.append({
                    'name': f"Apply security fix {idx + 1}",
                    'shell': command
                })
            
            playbook = {
                'hosts': 'all',
                'tasks': tasks
            }
            
            current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
            playbook_filename = f"correctif_{current_datetime}.yml"
            
            with open(playbook_filename, 'w') as file:
                yaml.safe_dump(playbook, file, sort_keys=False)
            return playbook_filename
        except Exception as e:
            raise Exception(f"Failed to generate Ansible playbook: {e}")
    
    def create_ability_template(self, ability_name, description, tactic, technique_id):
        """Crée un modèle de fichier YAML pour une ability Caldera."""
        try:
            template = {
                'name': ability_name,
                'description': description,
                'tactic': tactic,
                'technique': {
                    'attack_id': technique_id,
                    'name': 'Technique name placeholder'
                },
                'executor': {
                    'name': 'sh',
                    'command': 'echo "Command placeholder"'
                }
            }
            filename = f"{ability_name.lower().replace(' ', '_')}_ability.yml"
            with open(filename, 'w') as file:
                yaml.safe_dump(template, file, sort_keys=False)
            return filename
        except Exception as e:
            raise Exception(f"Failed to create ability template: {e}")
    
    def create_adversary_profile(self, name, description, abilities):
        """Crée un profil YAML pour un adversaire Caldera."""
        try:
            profile = {
                'name': name,
                'description': description,
                'abilities': abilities
            }
            filename = f"{name.lower().replace(' ', '_')}_adversary.yml"
            with open(filename, 'w') as file:
                yaml.safe_dump(profile, file, sort_keys=False)
            return filename
        except Exception as e:
            raise Exception(f"Failed to create adversary profile: {e}")
    
    def create_operation_profile(self, name, description, adversary_id, planner_id):
        """Crée un fichier YAML pour un profil d'opération Caldera."""
        try:
            profile = {
                'name': name,
                'description': description,
                'adversary': adversary_id,
                'planner': planner_id
            }
            filename = f"{name.lower().replace(' ', '_')}_operation.yml"
            with open(filename, 'w') as file:
                yaml.safe_dump(profile, file, sort_keys=False)
            return filename
        except Exception as e:
            raise Exception(f"Failed to create operation profile: {e}")

