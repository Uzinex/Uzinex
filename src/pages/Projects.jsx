import { useTranslation } from 'react-i18next';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { motion } from 'framer-motion';
import PageWrapper from '../components/PageWrapper';

const Projects = () => {
  const { t } = useTranslation();

  return (
    <PageWrapper>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
      >
        <Navbar />
        <motion.section id="projects" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
          <h1>{t('projects.title')}</h1>
          <ul className="project-list">
            <li>Uzcoin</li>
            <li>Freelance</li>
            <li>Host</li>
            <li>Bank</li>
          </ul>
        </motion.section>
        <Footer />
      </motion.div>
    </PageWrapper>
  );
};

export default Projects;
