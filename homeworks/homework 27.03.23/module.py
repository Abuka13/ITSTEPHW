models = ['заголовок','заголовок','заголовок','заголовок','заголовок','заголовок']


for i in range(len(models)):
    models[i] = models[i]+str(i+1)

#
new_models = []


for model in models:
    
    model_id = int(model[-1])
    if model_id % 2 == 0:
        new_models.append(model)


print(new_models)