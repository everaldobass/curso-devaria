# Devaria - Noções de Git

#### Devaria - aula 13 - Noções de Git - parte 1

#### Ferramenta GIT
- Existe diversas ferramentas para gerenciar e versionar o código fonte ou qualquer projeto.

#### Baixando o GIt
```
https://git-scm.com/
```
- Verificar a versão
```
- git --version
```
#### Devaria - aula 13 - Noções de Git - parte 2
- Atualmente, sabe trabalhar em equipe é algo muito importante. no entanto, muito além das competências técnicas.

#### O que é versionamento?
- O Versionamento de código é o gerenciamento de versões de um documento de texto qualquer.
- O Versionamento é controlado pelo oque chmamamos de sistema de contrle de versões. Normalmente, esses sistemas são utilizados no desenvolvimento de sotftware para controlar as diferentes versões e história de desenvolvimento do código.

#### Principais vantagens em versionar

#### Controle de histórico
- É possével visualizar toto o histórioco de desenvolvimento e voltar para versões abteriore. Além disso, temos a possibilidade de avaliar no detalhe o que foi mudado de uma versão para outra.

#### Trabalho em equipe
- Um Sistema de versionamento permite que várias pessoas trabalhem no mesmo conjunto de arquivos(repositório) ao mesmo tempo em que evita conflitos entre as alterações. Cada membro do time de desenvolvimento tem sua cópia dos arquivos que ao final das alterações é colocada junto das versões alteradas dos demais.

#### Marcação e resgate de verssões estáveis
- Através de padrões de nomeclatura para as ramificações do código no sercionamento. é possível identificar de forma fácil verssões especificas e quais oferecem código estável e quais ainda estão sob avaliação ou desenvolvimento.

#### Ramificação de projeto
- Esta é a base para versionamento. A possibilidade de ter várias linhas de desenvolvmimento paralelas sem que uma interfira na outra. Cada dev tem sua versão do código e pode alterá-la da forma como acha necessário sem receio de interferir no trabalho do seu time.

#### Segurança
- Os softwares de controle de verssão em geral possuem recursos para evitar invasões de agentes infecciosos nos arquivos. Somente usuários aos quais foi concedida permissão para edição do código conseguirão alterá-lo.

#### Confiança
Embora a finalidade das ferramentas de versionamento não seja a de oferecer um backup do código, mas sim seu histórioco e fácil navegação entre versões, ele pode acabar servindo para isto também. Normalmente os códigos versionados ficam em serviçoes hospedados na web que nos garantem que eles não serão perdidos. Assim temos ainda mais confiança de que nenhuma eventualidade poderá nos fazer perder o que já foi construído.

### Ferramenta
```
https://github.com/
```
- Github Desktop
- GitKraken

## Devaria - aula 13 - Noções de Git - parte 3

### Criar repositório
- Objetivo: Iniciar uma pasta como um repositório do git
- Quando Utilizar: Quando iniciamos um novo projeto, ou parte de um projeto que precisa ser isolada e gerenciada semparadamente.
- Ponto de atenção: Nunca crie um repositório dentro de outro, no git cada pasta/diretório raiz deve ser tratado como um repositório separatamente.

#### GIT INIT

```
- Comando para iniciar o git
git init

- Para adicionar os arquivo do git
git add .
```

#### Gerenciar arquivos
- Objetivo: Adcionar/Remover arquivos dentro deo repositório criado;
- Quando utilizar: Conforme formos trabalhando no dia a dia vamos subimos as atualizações do que stá local na no máquina;
Ponto de Atenção: A idéia é que vamos fazer diversos commits por dia.

- GIT STATUS
- GIT ADD - Nome do arquivo
- GIT ADD -A
- GIT COMMIT -M -"Comentários do que foi fetito"
- GIT PUSH
- GIT COMMIT -AM
- GIT REVERT - NUMERO DO COMMIT

```
git status
git diff nome do arquivo
git add nome do arquivo
git add .
git commit -m "Subir o arquivo"
git push
git add -a
git commit -am
git revert

```
### Gerenciar as arquivos Desktop

### Atualizar arquivos
- Objetivo: Capturar atualizações dos arquivos que foram criados no servidor e adicionar localmente;
- Quando utilizar: Conforme formos trabalhando no dia a dia vamos atualizar nosso repositório para que ele sempre esteja atualizado com os arquivos dos demais usuários;
- Ponto de atenção: Realizar essa atividade sempre antes de fazer um commit;

- GIT STATUS
- GIT PULL

```
git pull
```

### COMANDOS TEMPALTE
```

```










