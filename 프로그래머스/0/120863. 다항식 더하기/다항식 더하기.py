def solution(polynomial):
    lin = polynomial.split(' + ')  
    x_terms = [s for s in lin if 'x' in s]  
    constants = [int(s) for s in lin if 'x' not in s] 
    
    x_sum = 0
    for term in x_terms:
        if term == 'x':  
            x_sum += 1
        else:
            x_sum += int(term.replace('x', ''))  

    const_sum = sum(constants) 
    
    if x_sum != 0 :
        if x_sum == 1:
            if const_sum != 0 : 
                answer = f'x + {const_sum}'
            elif const_sum == 0 : 
                answer = 'x'
        else:
            if const_sum != 0 : 
                answer = f'{x_sum}x + {const_sum}'
            elif const_sum == 0 : 
                answer = f'{x_sum}x'
        
    if x_sum == 0 :
        if const_sum != 0 :
            answer = f'{const_sum}'
        elif const_sum == 0 :
            answer= ''
    
    return answer