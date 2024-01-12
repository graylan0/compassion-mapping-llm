import numpy as np
import matplotlib.pyplot as plt

def simulate_environmental_enrichment(init_well_being, intervention_strength, duration):
    time_steps = np.arange(0, duration, 1)
    well_being = [init_well_being]

    for t in time_steps:
        impact = intervention_strength * np.sin(t * np.pi / duration)  # Simulating cyclical impact
        new_well_being = well_being[-1] + impact
        well_being.append(new_well_being)

    return time_steps, well_being

def simulate_neuro_informed_intervention(init_well_being, genetic_sensitivity, intervention_effectiveness, duration):
    time_steps = np.arange(0, duration, 1)
    well_being = [init_well_being]

    for t in time_steps:
        impact = genetic_sensitivity * intervention_effectiveness * np.random.normal()  # Simulating personalized impact
        new_well_being = well_being[-1] + impact
        well_being.append(new_well_being)

    return time_steps, well_being

def simulate_combined_intervention(init_well_being, environmental_strength, genetic_sensitivity, intervention_effectiveness, duration):
    time_steps = np.arange(0, duration, 1)
    well_being = [init_well_being]

    for t in time_steps:
        environmental_impact = environmental_strength * np.sin(t * np.pi / duration)
        genetic_impact = genetic_sensitivity * intervention_effectiveness * np.random.normal()
        combined_impact = environmental_impact + genetic_impact
        new_well_being = well_being[-1] + combined_impact
        well_being.append(new_well_being)

    return time_steps, well_being

def simulate_community_support(init_well_being, engagement_strength, duration):
    time_steps = np.arange(0, duration, 1)
    well_being = [init_well_being]

    for t in time_steps:
        impact = engagement_strength * np.cos(t * np.pi / duration)  # Simulating community engagement impact
        new_well_being = well_being[-1] + impact
        well_being.append(new_well_being)

    return time_steps, well_being

def simulate_technological_mindfulness(init_well_being, mindfulness_strength, duration):
    time_steps = np.arange(0, duration, 1)
    well_being = [init_well_being]

    for t in time_steps:
        impact = mindfulness_strength * np.exp(-0.1 * t)  # Simulating the gradual impact of technological mindfulness
        new_well_being = well_being[-1] + impact
        well_being.append(new_well_being)

    return time_steps, well_being

# Example Usages:
initial_well_being = 0.6
duration_years = 10

# Scenario 1: Environmental Enrichment Initiative
intervention_strength_1 = 0.1
time_1, well_being_scenario_1 = simulate_environmental_enrichment(initial_well_being, intervention_strength_1, duration_years)

# Scenario 2: Personalized Neuro-Informed Intervention
genetic_sensitivity_2 = 0.8
intervention_effectiveness_2 = 0.2
time_2, well_being_scenario_2 = simulate_neuro_informed_intervention(initial_well_being, genetic_sensitivity_2, intervention_effectiveness_2, duration_years)

# Scenario 3: Combined Environmental and Neuro-Informed Intervention
environmental_strength_3 = 0.1
genetic_sensitivity_3 = 0.8
intervention_effectiveness_3 = 0.2
time_3, well_being_scenario_3 = simulate_combined_intervention(initial_well_being, environmental_strength_3, genetic_sensitivity_3, intervention_effectiveness_3, duration_years)

# Scenario 4: Community Engagement and Support
engagement_strength_4 = 0.15
time_4, well_being_scenario_4 = simulate_community_support(initial_well_being, engagement_strength_4, duration_years)

# Scenario 5: Technological Mindfulness Integration
mindfulness_strength_5 = 0.12
time_5, well_being_scenario_5 = simulate_technological_mindfulness(initial_well_being, mindfulness_strength_5, duration_years)

# Plotting all scenarios
plt.figure(figsize=(15, 10))

plt.subplot(3, 2, 1)
plt.plot(time_1, well_being_scenario_1, label="Environmental Enrichment")
plt.xlabel("Years")
plt.ylabel("Well-Being")
plt.title("Scenario 1: Environmental Enrichment Initiative")
plt.legend()

plt.subplot(3, 2, 2)
plt.plot(time_2, well_being_scenario_2, label="Neuro-Informed Intervention")
plt.xlabel("Years")
plt.ylabel("Well-Being")
plt.title("Scenario 2: Personalized Neuro-Informed Intervention")
plt.legend()

plt.subplot(3, 2, 3)
plt.plot(time_3, well_being_scenario_3, label="Combined Intervention")
plt.xlabel("Years")
plt.ylabel("Well-Being")
plt.title("Scenario 3: Combined Environmental and Neuro-Informed Intervention")
plt.legend()

plt.subplot(3, 2, 4)
plt.plot(time_4, well_being_scenario_4, label="Community Engagement and Support")
plt.xlabel("Years")
plt.ylabel("Well-Being")
plt.title("Scenario 4: Community Engagement and Support")
plt.legend()

plt.subplot(3, 2, 5)
plt.plot(time_5, well_being_scenario_5, label="Technological Mindfulness Integration")
plt.xlabel("Years")
plt.ylabel("Well-Being")
plt.title("Scenario 5: Technological Mindfulness Integration")
plt.legend()

plt.tight_layout()
plt.show()
