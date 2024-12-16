import argparse
from modules.caldera_module import CalderaAPI
from modules.ai_module import AIEngine

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script to interact with Caldera abilities, operations, and adversaries.')
    parser.add_argument('--abilities', action='store_true', help='List all available Caldera abilities.')
    parser.add_argument('--operations', action='store_true', help='List all running or completed operations in Caldera.')
    parser.add_argument('--adversary', action='store_true', help='List all adversaries in Caldera.')
    parser.add_argument('--recommendations', action='store_true', help='Generate Ansible playbooks to fix vulnerabilities.')
    parser.add_argument('--config', type=str, required=True, help='Path to the configuration file (config.yml).')
    return parser.parse_args()

def main():
    args = parse_arguments()
    caldera = CalderaAPI(config_path=args.config)
    ai_engine = AIEngine(config_path=args.config)
    
    if args.abilities:
        print("\n--- Fetching Abilities ---\n")
        try:
            abilities = caldera.get_abilities()
            for ability in abilities:
                print(f"Technique_id: {ability['technique_id']} | Tactic:{ability['tactic']} | Name: {ability['name']} | Description: {ability['description']}")
        except Exception as e:
            print(f"Error fetching abilities: {e}")
    
    if args.operations:
        print("\n--- Fetching Operations ---\n")
        try:
            operations = caldera.get_operations()
            for operation in operations:
                print(f"ID: {operation['id']} | Name: {operation['name']} | Status: {operation['state']}")
        except Exception as e:
            print(f"Error fetching operations: {e}")
    
    if args.adversary:
        print("\n--- Fetching Adversaries ---\n")
        try:
            adversaries = caldera.get_adversaries()
            for adversary in adversaries:
                print(f"ID: {adversary['adversary_id']} | Name: {adversary['name']} | TTPs: {adversary['description']}")
        except Exception as e:
            print(f"Error fetching adversaries: {e}")

    if args.recommendations:
        print("\n--- Generating Recommendations and Playbooks ---\n")
        try:
            operation_results = caldera.get_operations()
            recommendations = ai_engine.generate_bug_recommendations(operation_results)
            playbook_path = ai_engine.generate_ansible_playbook(recommendations)
            print(f"Ansible Playbook généré avec succès : {playbook_path}")
        except Exception as e:
            print(f"Erreur lors de la génération des playbooks Ansible : {e}")

if __name__ == "__main__":
    main()

