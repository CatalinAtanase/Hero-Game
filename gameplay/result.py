# Print the attack result
def result(attacker, defender, lucky, damage_done):
    print(
        f'''
            {attacker.name} has attacked {defender.name}.'''
    )

    if lucky:
        print('''
                However, the defender was lucky this time.'''
        )
    else:
        print(f''' 
                There was done a total of {damage_done if damage_done > 0 else 0} damage.
                {defender.name} {f"has {defender.health} health left." if defender.health > 0 else 'is dead.'}'''
        )
 