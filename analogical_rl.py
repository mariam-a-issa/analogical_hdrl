import env # placeholder for now
import math

# TODO: Calculates mapping
def phi(map):
    beta = #relative contribution of object
    object_sum = sum([struct_sim(o,map(o)) for o in state.objects])
    relation_sum = sum([struct_sim(r,map(r)) for r in state.relations])
    roles_sum =  # TODO
    return beta * object_sum +  relation_sum * (1 + roles_sum)

# Returns the similarity between state and exemplar
def struct_sim(s, e):
    sim = math.exp(theta * phi(max_map(s, e))) # TODO: some calculation
    return sim

# Returns the best mapping between state and exemplar
def max_map(state , exemplar):
    max_map = # TODO
    return max_map

def activation(s, e):
    return (e.attention * struct_sim(s, e)) / (sum([(e_prime.attention * struct_sim(s, e_prime)) for e_prime in exemplars]))

def est_value(s):
    return sum([e.value * activation(s, e) for e in exemplars])

class Exemplar: # i.e., concrete state exemplar
    def __init__(self):
        self.value = 0.0     # v(E); value of Exemplar
        self.attention = 0.0 # u(E); track which Exemplars to retain ~ voting weights, influence
        # TODO : fill out other values

def update_value(e):
    # TODO


''' Update attention
   - attention is increased for Exemplars increasing prediction accuracy
'''
def update_attention(e, td_error, sim_s_E, pred_diff):
    # td_error  = temporal difference error
    # sim_s_E   = struct sim between state and Exemplar
    # pred_diff = diff between Exemplar pred and overall pred: ~V
    e.attention += # TODO

# Need to do some class inheritance
class Schema:
    def __init__(self):
        self.value = 0.0     # v(E); value of schema

class State:
    def __init__(self):
        self.objects = None
        self.relations = None
        self.roles = None # TODO: this if going to be tricky

class TikTakToeGame:
    def __init__(self):

    def reset(self):

    def getAfterStates(self,state):
        return []



if __name__ == '__main__':
    exemplars = []  # List of Exemplar values

    # Hyperparameters
    theta = 0.0     # determines the specificity of generalization
    tau = 1.0       # exploration parameter

    env = TikTakToeGame.new()
    env.reset()
    while True:
        state = env.step()

        ''' TODO: A more realistic model would be more selective about which next states to loop through 
                 --> Note from paper (right now it loops through all)
        '''
        # get all next states (after state learning)
        next_states = env.getAfterStates()

        est_values = [est_value(s) for s in next_states]
        soft_max_values = [math.exp(v/tau) for v in est_values]

        #next_state = soft_max_values.index(max(soft_max_values))
        # TODO: Follow SARSA rule to pick next state/action

        # Produces TD Error --> update E values + attention via gradient descent
        for e in exemplars:
            update_attention(e)
            update_attention(e)
            #TODO: NOTE TO WHERE I LEFT OFF: WHAT TO DO AFTER GETTING TD ERROR



        # Pick next best state using a soft-max (Luce choice or Gibbs sampling rule)




        # creat_new_schema() if struct_sim(s, E) > inc_accuracy_threshold if E was not present
        # schema is abstract representation, defined by placeholder objects, shares on the shared info
        # that was mapped by the analogy. added to Exemplar pool, also has a value attached




